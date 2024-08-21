import sys
import time

from perthensis.gattc import bytesaddr, Central, UUID


SERVICE_UUID = UUID("226c0000-6476-4566-7562-66734470666d")
CHAR_UUID    = UUID("226caa55-6476-4566-7562-66734470666d")


def _call(cb, *args):
    try:
        cb(*args)
    except Exception as e:
        sys.print_exception(e)


class Value:
    def __init__(self, sensor, textval):
        self.sensor = sensor
        self.temp_c = self.hum_pcnt = None
        for part in textval.decode().strip("\x00 ").split(" "):
            try:
                kind, val = part.split("=", 1)
                val = float(val)
            except ValueError:
                continue
            if kind == "T":
                self.temp_c = val
            elif kind == "H":
                self.hum_pcnt = val


class Sensor:
    def __init__(self, central, addr, cb, name=None):
        self.peripheral = central.peripheral(addr, 0, self._connected, self._disconnected)
        self.cb = cb
        self.name = self.peripheral.hexaddr if name is None else str(name)
        self._charac = None
        self._value = None

    def _connected(self, peripheral):
        if peripheral is None:
            # Connection failed.
            _call(self.cb, Value(self, b""))
            return
        if self._charac is None:
            self.peripheral.discover_services(self._have_services, SERVICE_UUID)
        else:
            self._charac.enable_notify(self._notify)

    def _disconnected(self, peripheral):
        if self._value:
            _call(self.cb, self._value)
        self._value = None

    def _have_chars(self, svc):
        char = svc.get_characteristic(CHAR_UUID)
        if char:
            self._charac = char
            char.discover_descriptors(self._have_descrs)
        # TODO: else

    def _have_descrs(self, char):
        self._charac.enable_notify(self._notify)

    def _have_services(self, peripheral):
        svc = self.peripheral.get_service(SERVICE_UUID)
        if svc:
            svc.discover_characteristics(self._have_chars, CHAR_UUID)
        # TODO: else

    def _notify(self, charac, data):
        self._value = Value(self, bytes(data))
        self.peripheral.disconnect()

    @property
    def addr(self):
        return self.peripheral._addr

    @property
    def hexaddr(self):
        return self.peripheral.hexaddr

    def request_value(self):
        self.peripheral.connect()


class Sensors:
    def __init__(self, central, mapping, cb, status_cb=None):
        self._to_query = []
        self._querying = False
        self._nothing_since = time.time()
        self.sensors = []
        self.cb = cb
        self.status_cb = status_cb
        for addr, name in mapping.items():
            self.sensors.append(Sensor(central, addr, self._value, name))

    def _value(self, value):
        now = self._nothing_since = time.time()
        _call(self.cb, value)
        _call(self.status_cb, len(self.sensors) - len(self._to_query), len(self.sensors), now - self._querying)
        if len(self._to_query):
            self._to_query.pop().request_value()
        else:
            self._querying = False

    def request_all(self):
        if (time.time() - self._nothing_since) < 25 and self._querying:
            return False
        self._nothing_since = self._querying = time.time()
        self._to_query = list(reversed(self.sensors))
        self._to_query.pop().request_value()
        _call(self.status_cb, 0, len(self.sensors), 0)
        return True


class ScheduledSensors:
    def __init__(self, central, mapping, cb, status_cb=None, interval=60):
        self._sensors = Sensors(central, mapping, cb, status_cb)
        self._interval = interval

    async def schedule(self, sch):
        while True:
            _call(self._sensors.request_all)
            await sch.sleep(self._interval - (time.time() % self._interval))
