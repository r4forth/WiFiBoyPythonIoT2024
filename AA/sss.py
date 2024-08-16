import machine, os, sdcard

# Assign chip select (CS) pin (and start it high)
cs = machine.Pin(5, machine.Pin.OUT)
# Intialize SPI peripheral (start with 1 MHz)
spi = machine.SPI(2,
                  baudrate=1000000,
                  polarity=0,
                  phase=0,
                  bits=8,
                  firstbit=machine.SPI.MSB,
                  sck=machine.Pin(18),
                  mosi=machine.Pin(23),
                  miso=machine.Pin(19))
# Initialize SD card
sd = sdcard.SDCard(spi, cs)

# OR this simpler initialization code should works on Maker Pi Pico too...
#sd = sdcard.SDCard(machine.SPI(1), machine.Pin(15))

os.mount(sd, '/sd')
# check the content
os.listdir('/sd')

# try some standard file operations
file = open('/sd/test.txt', 'w')
file.write('Testing SD card on Maker Pi Pico')
file.close()
file = open('/sd/test.txt', 'r')
data = file.read()
print(data)
file.close()
