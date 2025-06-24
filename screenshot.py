import pyautogui
import time


time.sleep(0.5)
pyautogui.click(x=752, y=768)
time.sleep(0.5)
#----------------------------------------------

for i in range(1):
    screenshot = pyautogui.screenshot()
    pixels = screenshot.load()
    width, height = screenshot.size
    screenshot.save(f"red.png")


# -----------------------------------------------------------

'''
for i in range(200):
    screenshot = pyautogui.screenshot()
    # screenshot.save(f"screenshot.png")
    cropped = screenshot.crop((0,0,1280,800))
    cropped.save(f"./rune_test/test_3_{i}.png")
'''

# -----------------------------------------------------------
time.sleep(0.5)
pyautogui.click(x=812, y=758)
time.sleep(0.5)