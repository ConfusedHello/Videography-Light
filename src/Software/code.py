import time
import board
import keypad

import busio
import digitalio
import displayio
import terminalio

import adafruit_mcp4728
import adafruit_displayio_ssd1306

from adafruit_display_text import label


# I2C pins
SCL_PIN = board.SCL  # D5 / GPIO7
SDA_PIN = board.SDA  # D4 / GPIO6

# I2C addresses (7 bit addresses)
OLED_I2C_ADDR = 0x3C
DAC_I2C_ADDR = 0x60

# DAC pins
LDAC_PIN = board.A3  # GPIO29 - LDAC pin (must be held low to update DAC outputs immediately)
RDY_PIN = board.D6   # GPIO0 - RDY/BSY pin (indicates EEPROM write status, not used but pulled up)

# Button matrix pins
COL_PINS = (board.A0, board.A1, board.A2)
ROW_PINS = (board.D8, board.D7)

# Display dimensions
SCREEN_WIDTH = 128
SCREEN_HEIGHT = 64

# DAC output configuration
# Output range is from 0V to 3.3V (rail-to-rail)
# Output should be between 0.4V to 2.5V
# Output values are 16-bit in CircuitPython (0-65535)
MIN_DAC_VAL = int((0.4 / 3.3) * 65535)
MAX_DAC_VAL = int((2.5 / 3.3) * 65535)
OFF_DAC_VAL = 0

def brightness_to_dac(percent):
    """Converts a 0-100% brightness value to a 16-bit DAC value."""
    if percent <= 0:
        return OFF_DAC_VAL
    if percent >= 100:
        return MAX_DAC_VAL
    return MIN_DAC_VAL + int(((percent - 1) / 99.0) * (MAX_DAC_VAL - MIN_DAC_VAL))


# Initialise Display
displayio.release_displays()

# Initialise I2C bus
i2c = busio.I2C(SCL_PIN, SDA_PIN)

# Initialise DAC LDAC and RDY pins
ldac = digitalio.DigitalInOut(LDAC_PIN)
ldac.direction = digitalio.Direction.OUTPUT
ldac.value = False

rdy = digitalio.DigitalInOut(RDY_PIN)
rdy.direction = digitalio.Direction.INPUT
rdy.pull = digitalio.Pull.UP

# Initialise DAC and Display
display_bus = displayio.I2CDisplay(i2c, device_address=OLED_I2C_ADDR)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)

dac = adafruit_mcp4728.MCP4728(i2c, address=DAC_I2C_ADDR)

# Initialise button matrix
key_matrix = keypad.KeyMatrix(
    row_pins=ROW_PINS,
    column_pins=COL_PINS,
    columns_to_anodes=True
)
key_name_map = {0: "UP", 1: "SELECT", 2: "RIGHT", 3: "DOWN", 4: "LEFT"}

# Create a display group
ui_group = displayio.Group()
ui_labels = []

for i in range(1, 5):
    # Channel Name (eg. "> Ch A:")
    ch_label = label.Label(terminalio.FONT, text="", x=2, y=i * 16)
    ui_group.append(ch_label)

    # Percentage Value (e.g., "100%")
    val_label = label.Label(terminalio.FONT, text="", x=62, y=i * 16)
    ui_group.append(val_label)

    ui_labels.append((ch_label, val_label))

display.root_group = ui_group

def update_ui(brightness_levels, selected_channel):
    """Renders the user interface on the OLED display."""
    for i in range(4):
        selector = ">" if i == selected_channel else " "
        ch_name = chr(ord('A') + i)
        percent = brightness_levels[i]
        
        ui_labels[i][0].text = f"{selector}Ch {ch_name}:"
        ui_labels[i][1].text = f"{percent:3d}%"

# Ininitialise lights
brightness_levels = [20, 20, 20, 20]  # 0-100% for 4 channels
selected_channel = 0

# Set all channels to initial brightness
for i in range(4):
    dac_val = brightness_to_dac(brightness_levels[i])
    channel = getattr(dac, f'channel_{chr(ord("a") + i)}')
    channel.value = dac_val

update_ui(brightness_levels, selected_channel)

# Moved out of main loop for efficiency
key_name = None

# Main loop
while True:
    event = key_matrix.events.get()
    state_changed = False

    if event and event.pressed:
        key_name = key_name_map.get(event.key_number)

        if key_name == "UP":
            selected_channel = (selected_channel - 1) % 4
            state_changed = True
        elif key_name == "DOWN":
            selected_channel = (selected_channel + 1) % 4
            state_changed = True
        elif key_name == "RIGHT":
            brightness_levels[selected_channel] = min(100, brightness_levels[selected_channel] + 4)
            state_changed = True
        elif key_name == "LEFT":
            brightness_levels[selected_channel] = max(0, brightness_levels[selected_channel] - 4)
            state_changed = True
        elif key_name == "SELECT":
            # Toggle between 0% and 100% for quick on/off
            brightness_levels[selected_channel] = 100 if brightness_levels[selected_channel] == 0 else 0
            state_changed = True

    if state_changed and key_name in ["RIGHT", "LEFT", "SELECT"]:
        # Only update the DAC if brightness changed
        dac_val = brightness_to_dac(brightness_levels[selected_channel])
        channel = getattr(dac, f'channel_{chr(ord("a") + selected_channel)}')
        channel.value = dac_val
        
        # Update the display
        update_ui(brightness_levels, selected_channel)

    time.sleep(0.02)
