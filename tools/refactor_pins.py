import os
import re

CONFIG_IMPORT = "import wb_config"
CONFIG_FILE = "wb_config.py"
SOURCE_CONFIG = os.path.join("AA", CONFIG_FILE)
TARGET_CONFIG = os.path.join("DemoCode", CONFIG_FILE)

def replace_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # 1. Add import wb_config if not present
    if "import wb_config" not in content and "wb_config.Pins" not in content: # Avoid double import if re-run
        # Try to insert after imports
        import_match = re.search(r'^(import .*|from .* import .*)$', content, re.MULTILINE)
        if import_match:
            end_idx = import_match.end()
            content = content[:end_idx] + "\n" + CONFIG_IMPORT + content[end_idx:]
        else:
            content = CONFIG_IMPORT + "\n" + content

    # 2. Replacements based on context (Order matters: most specific first)
    replacements = [
        # Named arguments (strong context)
        (r'sda\s*=\s*Pin\(\s*23\b', 'sda=Pin(wb_config.Pins.I2C_SDA'),
        (r'scl\s*=\s*Pin\(\s*22\b', 'scl=Pin(wb_config.Pins.I2C_SCL'),
        (r'mosi\s*=\s*Pin\(\s*23\b', 'mosi=Pin(wb_config.Pins.SPI_MOSI'),
        (r'miso\s*=\s*Pin\(\s*19\b', 'miso=Pin(wb_config.Pins.SPI_MISO'),
        (r'sck\s*=\s*Pin\(\s*18\b', 'sck=Pin(wb_config.Pins.SPI_SCK'),
        (r'cs\s*=\s*Pin\(\s*5\b', 'cs=Pin(wb_config.Pins.SPI_CS'),
        (r'tx\s*=\s*Pin\(\s*5\b', 'tx=Pin(wb_config.Pins.UART_TX'),
        (r'rx\s*=\s*Pin\(\s*21\b', 'rx=Pin(wb_config.Pins.UART_RX'),

        # Machine module usage (strong context)
        (r'machine\.Pin\(\s*16\b', 'machine.Pin(wb_config.Pins.LED'),
        (r'machine\.Pin\(\s*27\b', 'machine.Pin(wb_config.Pins.BACKLIGHT'),
        (r'machine\.Pin\(\s*2\b', 'machine.Pin(wb_config.Pins.NEOPIXEL'), # Often used for NeoPixel
        (r'machine\.Pin\(\s*5\b', 'machine.Pin(wb_config.Pins.SPI_CS'),
        (r'machine\.Pin\(\s*21\b', 'machine.Pin(wb_config.Pins.SYN6988_BUSY'),
        (r'machine\.Pin\(\s*23\b', 'machine.Pin(wb_config.Pins.I2C_SDA'), # Default to I2C/SPI MOSI? Context needed.
        (r'machine\.Pin\(\s*22\b', 'machine.Pin(wb_config.Pins.I2C_SCL'),
        (r'machine\.Pin\(\s*18\b', 'machine.Pin(wb_config.Pins.SPI_SCK'),
        (r'machine\.Pin\(\s*19\b', 'machine.Pin(wb_config.Pins.SPI_MISO'),
        (r'machine\.Pin\(\s*17\b', 'machine.Pin(wb_config.Pins.SOUND_PWM'),

        # General usage (Pin(...))
        (r'Pin\(\s*16\b', 'Pin(wb_config.Pins.LED'),
        (r'Pin\(\s*27\b', 'Pin(wb_config.Pins.BACKLIGHT'),
        (r'Pin\(\s*23\b', 'Pin(wb_config.Pins.I2C_SDA'), # Default to I2C SDA
        (r'Pin\(\s*22\b', 'Pin(wb_config.Pins.I2C_SCL'),
        (r'Pin\(\s*19\b', 'Pin(wb_config.Pins.SPI_MISO'),
        (r'Pin\(\s*18\b', 'Pin(wb_config.Pins.SPI_SCK'),
        (r'Pin\(\s*5\b', 'Pin(wb_config.Pins.SPI_CS'),
        (r'Pin\(\s*21\b', 'Pin(wb_config.Pins.SYN6988_BUSY'), # Default to Busy (vs UART RX)
        (r'Pin\(\s*2\b', 'Pin(wb_config.Pins.IR_RECEIVER'), # Default to IR/Button
        (r'Pin\(\s*17\b', 'Pin(wb_config.Pins.SOUND_PWM'),

        # Special cases
        (r'Pin\(\s*25\s*,\s*2\b', 'Pin(wb_config.Pins.SOUND_DAC, 2'),
        (r'Pin\(\s*25\b', 'Pin(wb_config.Pins.SOUND_DAC'),

        # Variable names to pins (context based on variable name)
        (r'led\s*=\s*Pin\(\s*16\b', 'led=Pin(wb_config.Pins.LED'),
        (r'led1\s*=\s*Pin\(\s*16\b', 'led1=Pin(wb_config.Pins.LED'),
        (r'led2\s*=\s*Pin\(\s*27\b', 'led2=Pin(wb_config.Pins.BACKLIGHT'),
        (r'busyPin\s*=\s*machine\.Pin\(\s*21\b', 'busyPin=machine.Pin(wb_config.Pins.SYN6988_BUSY'),

        # Clean up possible double machine.Pin(wb_config...) if already replaced
        # No, regex is usually safe if careful.
    ]

    for pattern, replacement in replacements:
        content = re.sub(pattern, replacement, content)

    if content != original_content:
        print(f"Refactoring {filepath}")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    # Process AA/
    for root, dirs, files in os.walk("AA"):
        for file in files:
            if file.endswith(".py") and file != "wb_config.py":
                replace_in_file(os.path.join(root, file))

    # Process DemoCode/
    for root, dirs, files in os.walk("DemoCode"):
        for file in files:
            if file.endswith(".py") and file != "wb_config.py":
                replace_in_file(os.path.join(root, file))

    # Copy wb_config.py to DemoCode if not exists
    if os.path.exists(SOURCE_CONFIG):
        with open(SOURCE_CONFIG, 'r', encoding='utf-8') as src:
            data = src.read()
        with open(TARGET_CONFIG, 'w', encoding='utf-8') as dst:
            dst.write(data)
        print(f"Copied {SOURCE_CONFIG} to {TARGET_CONFIG}")

if __name__ == "__main__":
    main()
