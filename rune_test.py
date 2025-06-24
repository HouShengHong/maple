import pyautogui
import time
from PIL import Image
import my_common
import my_function
import random




'''
rune_test的範圍:
    (360,352,920,417)
rune_test_0的範圍:
    (360,352,425,417)
rune_test_1的範圍:
    (525,352,590,417)
rune_test_2的範圍:
    (690,352,755,417)
rune_test_3的範圍:
    (855,352,920,417)

全彩:
    黃:
        (255, 187, 0)
    紅:
        (255, 0, 68)
        (255, 0, 85) 最好
    綠:
        (170, 255, 0) 最好
        (187, 255, 0)

外黃內彩:
    外黃:
        (255, 204, 0)
    內綠:
        (17, 255, 0)
    內紅:
        (255, 0, 0)

'''
def rune_test_edges(rectangle:tuple[int,int,int,int]) -> list[tuple[int,int,int,int]]:
    (x1,y1,x2,y2) = rectangle
    top   = (x1,y1-1,x2,y1+2)
    down  = (x1,y2-2,x2,y2+1)
    left  = (x1-1,y1,x1+2,y2)
    right = (x2-1,y1,x2+2,y2)
    return[top,down,left,right]

def check_edge_color(pixels,rectangle:tuple[int,int,int,int]) -> str|None:
    for y in range(rectangle[1],rectangle[3]):
        for x in range(rectangle[0],rectangle[2]):
            match pixels[x,y]:
                case (255, 0, 85):
                    return "red"
                case (255, 0, 68):
                    return "red"
                case (170, 255, 0):
                    return "green"
                case (187, 255, 0):
                    return "green"
                case (255, 204, 0):
                    return "yellow"
                case _:
                    pass
    return None

def rune_test_mid_horizontal(rectangle:tuple[int,int,int,int]) -> tuple[int,int,int,int]:
    (x1,y1,x2,y2) = rectangle
    mid = (y1 + y2 -1)//2
    return(x1,mid-1,x2,mid+2)

def rune_test_mid_vertical(rectangle:tuple[int,int,int,int]) -> tuple[int,int,int,int]:
    (x1,y1,x2,y2) = rectangle
    mid = (x1 + x2 -1)//2
    return(mid-1,y1,mid+2,y2)

def check_mid_green(pixels,rectangle:tuple[int,int,int,int]) -> tuple[int,int]|None:
    for y in range(rectangle[1],rectangle[3]):
        for x in range(rectangle[0],rectangle[2]):
            match pixels[x,y]:
                case (17, 255, 0):
                    return (x,y)
                case _:
                    pass
    return None 

def check_mid_red(pixels,rectangle:tuple[int,int,int,int]) -> tuple[int,int]|None:
    for y in range(rectangle[1],rectangle[3]):
        for x in range(rectangle[0],rectangle[2]):
            match pixels[x,y]:
                case (255, 0, 0):
                    return (x,y)
                case _:
                    pass
    return None

def is_rune_test(pixels):
    list_rune_tests:list[tuple[int,int,int,int]] = [
        (360,352,425,417),
        (525,352,590,417),
        (690,352,755,417),
        (855,352,920,417),
    ]

    for rune_test in list_rune_tests:
        list_rune_test_edges = rune_test_edges(rune_test)
        list_rune_test_edges_colors:list[str|None] = []
        for rune_test_edge in list_rune_test_edges:
            color = check_edge_color(pixels,rune_test_edge) 
            list_rune_test_edges_colors.append(color)
        # print(list_rune_test_edges_colors) 
        match list_rune_test_edges_colors:
            case ["red","green",_,_]:
                return "down"
            case ["green","red",_,_]:
                return "up"
            case [_,_,"red","green"]:
                return "right"
            case [_,_,"green","red"]:
                return "left"
            case ["yellow","yellow","yellow","yellow"]:
                horizontal = rune_test_mid_horizontal(rune_test)
                red = check_mid_red(pixels,horizontal)
                green = check_mid_green(pixels,horizontal)
                match [red,green]:
                    case [(redX,redY),(greenX,greenY)]:
                        if (redX - greenX) > 0:
                            return "right"
                        else:
                            return "left"
                    case _:
                        pass
                vertical = rune_test_mid_vertical(rune_test)
                red = check_mid_red(pixels,vertical)
                green = check_mid_green(pixels,vertical)
                match [red,green]:
                    case [(redX,redY),(greenX,greenY)]:
                        if (redY - greenY) < 0:
                            return "up"
                        else:
                            return "down"
                    case _:
                        pass
            case _:
                pass
    return None
            














def find_runeTest_allColor_red(pixels,rectangle:tuple[int,int,int,int]):
    for y in range(352,417):
        for x in range(360,920):
            if pixels[x,y] == (255, 0, 85):
                return (x,y)
    for y in range(352,417):
        for x in range(360,920):
            if pixels[x,y] == (255, 0, 68):
                return (x,y)
    return None
def find_runeTest_allColor_green(pixels):
    for y in range(352,417):
        for x in range(360,920):
            if pixels[x,y] == (170, 255, 0):
                return (x,y)
    for y in range(352,417):
        for x in range(360,920):
            if pixels[x,y] == (187, 255, 0):
                return (x,y)
    return None
def find_runeTest_insideColor_red(pixels):
    for y in range(352,417):
        for x in range(360,920):
            if pixels[x,y] == (255, 0, 0):
                return (x,y)
    return None
def find_runeTest_insideColor_green(pixels):
    for y in range(352,417):
        for x in range(360,920):
            if pixels[x,y] == (17, 255, 0):
                return (x,y)
    return None

# -------------------------------------------------------------


time.sleep(0.5)
pyautogui.click(x=752, y=768)
time.sleep(0.5)

# -------------------------------------------------------------

# img = Image.open("./rune_test_1/_test_0_0.png")
# cropped = img.crop((360,352,426,417))
# cropped.save("rune_test_0.png")
# cropped = img.crop((525,352,591,417))
# cropped.save("rune_test_1.png")
# cropped = img.crop((690,352,756,417))
# cropped.save("rune_test_2.png")
# cropped = img.crop((854,352,920,417))
# cropped.save("rune_test_3.png")

#---------------------test-------------------------------------


# img = Image.open("./rune_test/test_3_0.png")
# img = Image.open("./rune_test_0.png")

# rune_test_0 = (360,352,425,417)
# rune_test_1 = (525,352,590,417)
# rune_test_2 = (690,352,755,417)
# rune_test_3 = (855,352,920,417)

# cropped = img.crop(rune_test_3)
# cropped.save('zzz.png')
# width, height = cropped.size
# pixels = cropped.load()

# for y in range(0,1):
#     for x in range(width):
#         print((x,y),pixels[x,y])

# width, height = img.size
# pixels = img.load()
# list_edge = rune_test_edges(rune_test_3)
# for edge in list_edge:
#     r = check_edge(pixels,edge)
#     print(r)

r = 1
while r is not None:
    if my_function.interrupt_by_key():
        break
    screenshot = pyautogui.screenshot()
    pixels = screenshot.load()
    r = is_rune_test(pixels)
    match r:
        case "up":
            my_function.hold_key(my_common.direction.up,hold_time=0.1)
            time.sleep(3)
        case "down":
            my_function.hold_key(my_common.direction.down,hold_time=0.1)
            time.sleep(3)
        case "left":
            my_function.hold_key(my_common.direction.left,hold_time=0.1)
            time.sleep(3)
        case "right":
            my_function.hold_key(my_common.direction.right,hold_time=0.1)
            time.sleep(3)
        case _:
            pass

        
# -----------------------------------------------------------

time.sleep(0.5)
pyautogui.click(x=812, y=758)
time.sleep(0.5)