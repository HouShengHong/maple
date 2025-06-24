from PIL import Image
import pyautogui
import time

def Hp_precent(pixels) -> float:
    for x in range(496,337,-1):
        for y in range(715,717):
            if pixels[x,y] == (255, 0, 0):
                return (x - 338) / 158
    return 0

time.sleep(0.5)
pyautogui.click(x=752, y=768)
time.sleep(0.5)




screenshot = pyautogui.screenshot()
pixels = screenshot.load()
width, height = screenshot.size
r = Hp_precent(pixels)
print(r)
screenshot.save("red.png")

time.sleep(0.5)
pyautogui.click(x=812, y=758)
time.sleep(0.5)
