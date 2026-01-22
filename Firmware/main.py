import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Macros

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

PINS = [
    board.D3,  # Row 1 - Key 1
    board.D4,  # Row 1 - Key 2
    board.D2,  # Row 1 - Key 3
    board.D1,  # Row 2 - Key 1
    board.D5,  # Row 2 - Key 2
    board.D6,  # Row 2 - Key 3
]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

keyboard.keymap = [
    [
        KC.SPACE,   # Row 1 - Left
        KC.UP,      # Row 1 - Middle
        KC.LGUI,    # Row 1 - Right (Windows)

        KC.LEFT,    # Row 2 - Left
        KC.DOWN,    # Row 2 - Middle
        KC.RIGHT,   # Row 2 - Right
    ]
]

if __name__ == '__main__':
    keyboard.go()
