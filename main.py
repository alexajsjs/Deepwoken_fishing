import pynput
import keyboard
import time


mouse = pynput.mouse.Controller()
while True:
    if keyboard.is_pressed("a") or keyboard.is_pressed("d") or keyboard.is_pressed("s"):
        mouse.click(pynput.mouse.Button.left)
        time.sleep(.036)
