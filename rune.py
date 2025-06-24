import time
import my_common
import my_function
import random
import pyautogui
import easyocr
from PIL import Image
import numpy as np



time.sleep(0.5)
pyautogui.click(x=752, y=768)
time.sleep(0.5)

# -------------------------------------------------------------


screenshot = pyautogui.screenshot()
reader = easyocr.Reader(['ch_tra', 'en'])  # 支援繁體中文與英文
screenshot_np = np.array(screenshot)
results = reader.readtext(screenshot_np)

# 顯示結果
for bbox, text, confidence in results:
    print(f"辨識文字：{text}（信心度：{confidence:.2f}）")

        # -----------------------------------------------------------

time.sleep(0.5)
pyautogui.click(x=812, y=758)
time.sleep(0.5)
