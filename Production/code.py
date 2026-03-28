import board
import busio
import displayio
import adafruit_ssd1306
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.matrix import DiodeOrientation
from kmk.modules.rgb import RGB
from kmk.modules.mouse_keys import MouseKeys

keyboard = KMKKeyboard()

keyboard.row_pins = (board.D0, board.D3, board.D6, board.D8)
keyboard.col_pins = (board.D1, board.D2, board.D4, board.D5)
keyboard.diode_orientation = DiodeOrientation.ROW2COL

# Mouse
keyboard.modules.append(MouseKeys())

# RGB LEDs
rgb = RGB(pixel_pin=board.D7, num_pixels=32)
keyboard.modules.append(rgb)

# OLED logo
i2c = busio.I2C(board.D5, board.D4)
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
displayio.release_displays()

with open("/logo.bmp", "rb") as f:
    bmp = displayio.OnDiskBitmap(f)
    face = displayio.TileGrid(bmp, pixel_shader=bmp.pixel_shader)
    splash = displayio.Group()
    splash.append(face)
    oled.show(splash)

# Keymap
keyboard.keymap = [
    [
        KC.SLEP,       KC.UNDO,    KC.FIND,    KC.MUTE,
        KC.COPY,       KC.PASTE,   KC.LCTL(KC.A), KC.F3,
        KC.MS_WH_UP,   KC.MS_BTN2, KC.UP,      KC.F5,
        KC.MS_WH_DOWN, KC.LEFT,    KC.DOWN,    KC.RIGHT
    ]
]

if __name__ == '__main__':
    keyboard.go()
