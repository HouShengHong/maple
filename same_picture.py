from PIL import Image
import pyautogui
import time

def same_img(img_0,img_1):
        img_0 = Image.open(img_0)
        img_1 = Image.open(img_1)
        width, height = img_0.size
        img_0 = img_0.load()
        img_1 = img_1.load()
        for y in range(5,6):
            for x in range(0,68):
                if img_0[x,y] != img_1[x,y]:
                     print((x,y))
                     return False
                else:
                     pass
        return True

def rune_on(img):
    img = Image.open(img)
    img = img.load()
    y = 119
    for x in range(635,647):
        if img[x,y] != (254, 254, 254):
            return False
    y = 127
    for x in range(635,647):
        if img[x,y] != (255, 255, 255):
            return False
    return True
        
def find_color_sequence(screenshot, pixels):
    width, height = screenshot.size
    target_sequence = [(34, 34, 34), (255, 255, 255), (255, 255, 255), (230, 239, 252), (100, 154, 236), (97, 163, 229), (255, 255, 255), (244, 248, 255), (169, 200, 247), (43, 125, 222), (43, 125, 222), (43, 125, 222), (43, 125, 222), (43, 125, 222), (43, 125, 222), (111, 166, 233), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (182, 209, 242), (58, 131, 222), (82, 150, 229), (169, 204, 246), (206, 222, 255), (191, 215, 248), (110, 166, 231), (54, 130, 222), (138, 180, 238), (206, 222, 255), (206, 222, 255), (206, 222, 255), (233, 240, 255), (255, 255, 255), (255, 255, 255), (189, 217, 245), (151, 190, 239), (216, 229, 249), (255, 255, 255), (245, 245, 255), (134, 176, 234), (76, 141, 222), (195, 217, 244), (255, 255, 255), (117, 175, 232), (46, 129, 222), (125, 171, 234), (229, 237, 251), (255, 255, 255), (255, 255, 255), (255, 255, 255), (191, 217, 242), (161, 193, 239), (157, 190, 239), (157, 190, 239), (157, 190, 239), (157, 190, 239), (157, 190, 239), (242, 246, 253), (255, 255, 255), (64, 137, 226), (57, 139, 222), (239, 246, 252), (255, 255, 255), (255, 255, 255), (11, 11, 11), (11, 11, 11)]
    target_sequence = target_sequence[1:4]
    seq_len = len(target_sequence)

    # 掃描每一列
    for y in range(height):
        for x in range(width - seq_len + 1):
            match = True
            for i in range(seq_len):
                if pixels[x + i, y] != target_sequence[i]:
                    match = False
                    break
            if match:
                # print(f"找到匹配序列：起始位置 = ({x}, {y})")
                return (x, y)
    
    # print("找不到該顏色序列")
    return None
    
def get_region_pixels(pixels, x, y, w, h):
    result = []
    for dy in range(h):
        row = []
        for dx in range(w):
            row.append(pixels[x + dx, y + dy])
        result.append(row)
    return result

def region_match(pixels, x, y, pattern):
    for dy, row in enumerate(pattern):
        for dx, target_color in enumerate(row):
            if pixels[x + dx, y + dy] != target_color:
                return False
    return True

def find_region(image_b,screenshot, pattern):
    """在 B 圖中搜尋 pattern 是否存在，回傳位置"""
    width, height = screenshot.size
    pattern_h = len(pattern)
    pattern_w = len(pattern[0]) if pattern else 0

    for y in range(height - pattern_h + 1):
        for x in range(width - pattern_w + 1):
            if region_match(image_b, x, y, pattern):
                return (x, y)
    return None

'''
for i in range(199):
    r = same_img(f"./rune/rune_{i}.png",f"./rune/rune_{i + 1}.png")
    if r:
        pass
    else:
        print(i,r)
'''

'''
img = Image.open("./rune/rune_0.png")
pixels = img.load()
l = []
for x in range(68):
    l.append(pixels[x,5])

print(l)
'''



time.sleep(0.5)
pyautogui.click(x=752, y=768)
time.sleep(0.5)

# -------------------------------------------------------------
img = Image.open("./rune/rune_0.png")
img = img.load()
pattern = get_region_pixels(img, 10, 10, 1, 1)



screenshot = pyautogui.screenshot()
pixels = screenshot.load()
width, height = screenshot.size
r =  find_region(pixels,screenshot, pattern)



r = find_color_sequence(screenshot,pixels)
print(r)


# -----------------------------------------------------------

time.sleep(0.5)
pyautogui.click(x=812, y=758)
time.sleep(0.5)
