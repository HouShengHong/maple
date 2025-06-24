import pyautogui
from PIL import Image
import time




# time.sleep(0.5)
# pyautogui.click(x=752, y=768)
# time.sleep(0.5)

# -------------------------------------------------------------

img = Image.open("screenshot.png")
# img = pyautogui.screenshot()
# img.save("123.png")
width, height = img.size
gray_image = img.convert('L')
pixels = gray_image.load()

'''
for x in range(width):
    for y in range(height):
        old_value = pixels[x, y]
        new_value = max(0, old_value - 250)  
        pixels[x, y] = new_value
# gray_image.save('screenshot_darkened.png')

# 保存灰阶图像（可选）
# gray_image.save('screenshot_gray.png')
'''

# -----------------------------------------------------------

# time.sleep(0.5)
# pyautogui.click(x=812, y=758)
# time.sleep(0.5)