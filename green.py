import pyautogui
import time
from PIL import Image
import my_common
import my_function
import random

# green 350 < y < 500x

def find_green(pixels,screenshot) -> tuple[int,int,] | None:
    width, height = screenshot.size
    # for y in range(height): 
    for y in range(350,500): 
        for x in range(width):
            if pixels[x, y] == (64, 204, 71):
                return(x,y)
    return None
# ---------------------------------------------
time.sleep(0.5)
pyautogui.click(x=752, y=768)
time.sleep(0.5)
# ---------------------------------------------
for i in range(1):
    # my_function.hold_key(my_common.key_map.health)
    # time.sleep(0.1)
    screenshot = pyautogui.screenshot()
    pixels = screenshot.load()
    g = find_green(pixels,screenshot)
    match g:
        case (_,y):
            print(y)
        case _:
            print(g)
# ---------------------------------------------
time.sleep(0.5)
pyautogui.click(x=812, y=758)
time.sleep(0.5)