from micropython import const
import asyncio
import aioble
import bluetooth
import struct
from machine import Pin
from random import randint

# 啟動玩學機內建的 LED
led = Pin(16, Pin.OUT)
led.value(0)

# 設定隨機數值
value = 0

# 這個站點可以產生 UUIDs:
# https://www.uuidgenerator.net/
_BLE_SERVICE_UUID = bluetooth.UUID('C8B038B0-0C8E-4525-92B9-17482205970B')
_BLE_SENSOR_CHAR_UUID = bluetooth.UUID('C8B038B0-0C8E-4525-92B9-17482205970B')
_BLE_LED_UUID = bluetooth.UUID('C8B038B0-0C8E-4525-92B9-17482205970B')
# How frequently to send advertising beacons.
_ADV_INTERVAL_MS = 250_000

# 註冊 GATT 伺服器的服務與特徵值
ble_service = aioble.Service(_BLE_SERVICE_UUID)
sensor_characteristic = aioble.Characteristic(ble_service, _BLE_SENSOR_CHAR_UUID, read=True, notify=True)
led_characteristic = aioble.Characteristic(ble_service, _BLE_LED_UUID, read=True, write=True, notify=True, capture=True)

# 註冊服務
aioble.register_services(ble_service)

# 將數據進行編碼成 UTF-8 格式
def _encode_data(data):
    return str(data).encode('utf-8')

# 當其他設備寫入  led_characteristic 資料將用位元組的格式
def _decode_data(data):
    try:
        if data is not None:
            number = int.from_bytes(data, 'big')
            return number
    except Exception as e:
        print("Error decoding temperature:", e)
        return None

# 模擬溫度計的讀數
def get_random_value():
    return randint(19, 40)

# 取得新的溫度資料並更新數值
async def sensor_task():
    while True:
        value = get_random_value()
        sensor_characteristic.write(_encode_data(value), send_update=True)
        print('目前的溫度資料為: ', value)
        await asyncio.sleep_ms(1000)
        
async def peripheral_task():
    while True:
        try:
            async with await aioble.advertise(
                _ADV_INTERVAL_MS,
                name="OK!ESP32",
                services=[_BLE_SERVICE_UUID],
                ) as connection:
                    print("Connection from", connection.device)
                    await connection.disconnected()             
        except asyncio.CancelledError:
            print("Peripheral task cancelled")
        except Exception as e:
            print("Error in peripheral_task:", e)
        finally:
            await asyncio.sleep_ms(100)

async def wait_for_write():
    print("wait_for_write task started")  # 确认任务启动
    while True:
        try:
            connection, data = await led_characteristic.written()
            print("Received data:", data)  # 打印收到的数据
            print("Data type:", type(data))  # 打印数据类型
            data = _decode_data(data)
            print('Connection: ', connection)
            print('Data: ', data)
            if data == 1:
                print('開啟 LED')
                led.value(0)
            elif data == 0:
                print('關閉 LED')
                led.value(1)
            else:
                print('未知的命令')
        except asyncio.CancelledError:
            print("wait_for_write task cancelled")
        except Exception as e:
            print("Error in wait_for_write:", e)
        finally:
            await asyncio.sleep_ms(100)            
# Run tasks
async def main():
    t1 = asyncio.create_task(sensor_task())
    t2 = asyncio.create_task(peripheral_task())
    t3 = asyncio.create_task(wait_for_write())
    await asyncio.gather(t1, t2)
    
asyncio.run(main())