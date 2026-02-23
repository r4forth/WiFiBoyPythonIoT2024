# wb_config.py
import sys
import os

# Detect board
try:
    import machine
    # Note: This detection might need adjustment based on actual firmware string
    # Typical strings: "ESP32S3 module with ESP32S3"
    IS_ESP32S3 = 'ESP32S3' in os.uname().machine
except:
    IS_ESP32S3 = False # Default to ESP32 if detection fails or running in simulator without machine

class Pins:
    if IS_ESP32S3:
        # Configuration for ESP32-S3 (WiFiBoy Python IoT 2024)
        # These are placeholders! Update with actual pinout if known.
        # Assuming typical S3 usage or remapping required.

        # On-board LED
        LED = 2  # GPIO 2 is common for built-in LED on S3
        BACKLIGHT = 10 # Example placeholder for backlight

        # I2C (SDA, SCL)
        # Note: Pins 8, 9 are often used for I2C on S3 DevKitC-1
        I2C_SDA = 8
        I2C_SCL = 9

        # SPI (Often SPI2 / FSPI)
        # Note: Pins 11, 12, 13 are often used for SPI on S3 DevKitC-1
        SPI_MISO = 13
        SPI_MOSI = 11
        SPI_SCK = 12
        SPI_CS = 10

        # UART (Often UART1)
        # Note: Pins 43, 44 are often used for UART on S3 DevKitC-1
        UART_TX = 43
        UART_RX = 44

        # Button Inputs
        BUTTON_A = 0 # Boot button
        BUTTON_B = 14 # Example

        # Sound / Buzzer / DAC
        # ESP32-S3 does NOT have a DAC. Use PWM instead.
        SOUND = 17 # PWM capable pin
        SOUND_PWM = 17
        SOUND_DAC = 18 # Placeholder, S3 has no DAC.

        # SYN6988 Busy Pin
        SYN6988_BUSY = 21 # Keep same if possible, or update

        # Other potential pins
        IR_RECEIVER = 2 # Example
        NEOPIXEL = 2 # Example

    else:
        # Configuration for ESP32 (Original WiFiBoy Python IoT)
        LED = 16
        BACKLIGHT = 27

        I2C_SDA = 23
        I2C_SCL = 22

        # Note: SPI on ESP32 typically uses these pins
        SPI_MISO = 19
        SPI_MOSI = 23
        SPI_SCK = 18
        SPI_CS = 5

        UART_TX = 5
        UART_RX = 21

        BUTTON_A = 2 # Often used
        BUTTON_B = 5 # Often used

        SOUND = 17
        SOUND_PWM = 17
        SOUND_DAC = 25 # ESP32 has DAC on 25

        SYN6988_BUSY = 21

        IR_RECEIVER = 2
        NEOPIXEL = 2

# Helper to check if S3
def is_s3():
    return IS_ESP32S3
