try:
    from win32api import GetAsyncKeyState as getState
except ModuleNotFoundError:
    raise Exception("You do not have pywin32 installed. Get it from: https://github.com/mhammond/pywin32/releases")

key = { #keycodes from the MSDN
    "TAB": 9,
    "ENTER": 13,
    "SHIFT": 16,
    "CONTROL": 17,
    "ALT": 18,
    "ESCAPE": 27,
    "SPACE": 32,
    "LEFT": 37,
    "UP": 38,
    "RIGHT": 39,
    "DOWN": 40
}

for k in range(65,90): #getting key codes for letter keys
    key[chr(k)] = k

for k in range(48,57): #getting key codes for number keys
    key[chr(k)] = k

def isPressed(keycode): #simple async keyboard polling function
    return False if getState(keycode) == 0 else True