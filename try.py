import pyautogui
import time
from PIL import Image
import my_common
import my_function
import random

# 軍一小地圖範圍 (0, 30, 137, 290)
# 遺跡之墓2小地圖範圍 (0,30,181,226)
# layer 4 y = 160-161
# layer 3 y = 185-187
# layer 2 y = 201-202
# layer 1 y = 221-226
# layer 0 y = 253-259
'''
遺跡之墓2
小地圖範圍 (0,30,181,226)
小地圖[4,225] - [177,225] 是(255,255,255)

layer_0
y = 187, 95  <= x <= 100 -> 右上跳
y = 187, 101 <= x <= 105 -> 上跳
y = 187, 106 <= x <= 111 -> 左上跳

layer_1
y = 165, 100 <= x <= 106 -> 上瞬

layer_2
y = 150, 105 <= x <= 110 -> 上

'''



'''
遺跡之墓2小地圖[4,225] - [177,225] 是(255,255,255)
軍一小地圖[2,289] - [135,289] 是(255,255,255)
screenshot = pyautogui.screenshot()
pixels = screenshot.load()
# cropped = screenshot.crop((0, 30, 137, 290))
# pixels = cropped.load()

for x in range(2,136):
    if pixels[x,289] != (255,255,255):
        print("error")
'''                                                         
def Hp_precent(pixels) -> float:
    for x in range(496,337,-1):
        for y in range(715,717):
            if pixels[x,y] == (255, 0, 0):
                return (x - 338) / 158
    return 0

def change_channel():       
    pyautogui.click(x=1136, y=708,duration=random.uniform(0.2,0.5))
    pyautogui.click(x=1136, y=651,duration=random.uniform(0.2,0.4))
    pyautogui.click(x=866, y=160,duration=random.uniform(0.2,0.5))
    pyautogui.click(x=594, y=420,duration=random.uniform(0.2,0.5))

def launch_game():
    pyautogui.click(x=867, y=390)
    time.sleep(3)
    pyautogui.click(x=870, y=276)

def yellowX_mapping_realX(yellowX:int) -> float | None:
    match yellowX:
        case yellowX if 40 <= yellowX <= 98:
            return 180 + (yellowX - 40) * 15.6
        case _ :
            return None

def realX_mapping_yellowX(realX:int) -> int | None :
    yellowX = (realX - 180) / 15.6 + 40
    yellowX = int(round(yellowX))
    match yellowX:
        case yellowX if 40 <= yellowX <= 98:
            return int(round(yellowX))
        case yellowX if yellowX < 40:
            return 40
        case yellowX if yellowX > 98:
            return 98
        case _:
            return None

def is_rune_on(pixels) -> bool:
    y = 119
    for x in range(635,647):
        if pixels[x,y] != (254, 254, 254):
            return False
    y = 127
    for x in range(635,647):
        if pixels[x,y] != (255, 255, 255):
            return False
    return True

def routine_operation(
        direction:str = my_common.direction.right, 
        walk_time:float = random.uniform(0.7,0.9),
        health_or_not:bool = True,
        health_time:float = random.uniform(0.6,1.1 ), 
        sleep_time:float = 0
    ) -> None:
    my_function.hold_key(direction,hold_time=walk_time)
    if health_or_not:
        my_function.hold_key(my_common.key_map.health,hold_time=health_time)
    time.sleep(sleep_time)

def am_i_inside(pixels) -> tuple | None:
    y = 289
    for x in range(2,135):
        if pixels[x,y] != (255,255,255):
            return None
    return find_yellow_in_smallMap_inside(pixels)
    
def am_i_outside(pixels) -> tuple | None:
    y = 225
    for x in range(4,177):
        if pixels[x,y] != (255,255,255):
            return None
    return find_yellow_in_smallMap_outside(pixels)

def how_should_i_do_outside(x,y):        
    match y:
        case 187:
            match x:
                case x if 95 <= x <= 100:
                    my_function.hold_key(my_common.direction.right, my_common.key_map.jump, hold_time=0.03)
                    my_function.hold_key(my_common.direction.up, hold_time=0.1)
                case x if 101 <= x <= 104:
                    my_function.hold_key(my_common.direction.up, my_common.key_map.jump, hold_time=0.1)
                    my_function.hold_key(my_common.direction.up, hold_time=0.1)
                case x if 105 <= x <= 111:
                    my_function.hold_key(my_common.direction.left, my_common.key_map.jump, hold_time=0.03)
                    my_function.hold_key(my_common.direction.up, hold_time=0.1)
                case x if x < 95:
                    my_function.hold_key(my_common.direction.right, hold_time=0.2)
                case x if x > 111:
                    my_function.hold_key(my_common.direction.left, hold_time=0.2)
        case y if 165 < y < 186:
            match x:
                case 103:
                    my_function.hold_key(my_common.direction.up,my_common.key_map.flash, hold_time=0.5)
                case _:
                    my_function.hold_key(my_common.direction.right, my_common.direction.down, my_common.key_map.jump, hold_time=0.03)
        case 165:
            match x:
                case x if 100 <= x <= 105:
                    my_function.hold_key(my_common.direction.up,my_common.key_map.flash, hold_time=0.1)
                case x if x < 100:
                    my_function.hold_key(my_common.direction.right, hold_time=0.2)
                case x if x > 105:
                    my_function.hold_key(my_common.direction.left, hold_time=0.1)
        case 150:
             match x:
                case x if 105 <= x <= 110:
                    my_function.enter_light()
                case x if x < 105:
                    my_function.hold_key(my_common.direction.right, hold_time=0.2)
                case x if x > 110:
                    my_function.hold_key(my_common.direction.left, hold_time=0.2)
        case _:
            my_function.hold_key(my_common.direction.right,my_common.direction.down,my_common.key_map.jump, hold_time=0.2)

def which_layer_inside(y):
    match y:
        case y if y < 160:
            return 4.5       
        case y if 160 <= y <= 161:  # layer_4
            return 4        
        case y if 161 < y < 185:
            return 3.5        
        case y if 185 <= y <= 187:  # layer_3
            return 3          
        case y if 187 < y < 201:
            return 2.5       
        case y if 201 <= y <= 202:  # layer_2 
            return 2      
        case y if 202 < y < 221:
            return 1.5       
        case y if 221 <= y <= 226:  # layer_1  
            return 1          
        case y if 226 < y < 253:
            return 0.5        
        case y if 253 <= y <= 259:
            return 0 
        case _:
            return -1                 
    
def i_am_near_greenHp_flash(direction):
    shining_ray_time = random.uniform(0.1,0.2)
    sleep_time_1 = random.uniform(0,0.05)
    # press direction
    sleep_time_2 = random.uniform(0.1,0.2)
    flash_time = random.uniform(0.1,0.2)
    sleep_time_3 = random.uniform(0,0.05)
    # keyUp shining_ray
    sleep_time_4 = random.uniform(0,0.1)

    my_function.hold_key(my_common.key_map.shining_ray,hold_time=shining_ray_time)
    time.sleep(sleep_time_1)
    pyautogui.keyDown(direction)
    time.sleep(sleep_time_2)
    my_function.hold_key(my_common.key_map.flash,hold_time=flash_time)
    time.sleep(sleep_time_3)
    pyautogui.keyUp(direction)
    time.sleep(sleep_time_4)    
    
    # my_function.hold_key(my_common.key_map.health,hold_time=health_time)
    # time.sleep(sleep_time_5)
    # pyautogui.keyUp(direction)
    # time.sleep(sleep_time_6)

def i_am_near_greenHp_walk(direction):
    oppositeDirection =my_function.opposite_direction(direction)
    # total_time = random.uniform(2.2,2.5)

    walk_time = random.uniform(1.6,2.1)
    sleep_time_1 = random.uniform(0,0.05)
    shining_ray_time = random.uniform(0.3,0.6)
    sleep_time_2 = max(walk_time - sleep_time_1 - shining_ray_time,0)


    sleep_time_3 = random.uniform(0,0.05)
    health_time = random.uniform(0.1,0.3)
    sleep_time_4 = random.uniform(0,0.05)
    sleep_time_5 = random.uniform(0,0.05)


    pyautogui.keyDown(direction)
    time.sleep(sleep_time_1)
    my_function.hold_key(my_common.key_map.shining_ray,hold_time=shining_ray_time)
    time.sleep(sleep_time_2)
    pyautogui.keyUp(direction)

  

    pyautogui.keyDown(oppositeDirection)
    time.sleep(sleep_time_3)
    my_function.hold_key(my_common.key_map.health,hold_time=health_time)
    time.sleep(sleep_time_4)
    pyautogui.keyUp(oppositeDirection)
    time.sleep(sleep_time_5)

    # ---
    # time.sleep(sleep_time_4)
    # my_function.hold_key(my_common.key_map.health,hold_time=health_time)
    # time.sleep(sleep_time_5)
    # time.sleep(sleep_time_6)
    
def i_am_NOT_near_greenHp_flash(direction):
    pyautogui.keyDown(direction)
    time.sleep(random.uniform(0,0.05))
    my_function.hold_key(my_common.key_map.flash,hold_time=random.uniform(0.05,0.1))
    time.sleep(random.uniform(0.05,0.1))
    my_function.hold_key(my_common.key_map.shining_ray,hold_time=random.uniform(0.3,0.5))
    time.sleep(random.uniform(0.1,0.2))
    pyautogui.keyUp(direction)    
    time.sleep(random.uniform(0,0.05))

def i_am_NOT_near_greenHp_walk(direction):
    oppositeDirection =my_function.opposite_direction(direction)

    sleep_time_3 = random.uniform(0,0.05)
    health_time = random.uniform(0.2,0.4)
    sleep_time_4 = random.uniform(0,0.05)
    sleep_time_5 = random.uniform(0,0.05)



    my_function.hold_key(direction,hold_time=random.uniform(0.8,1.2))
    time.sleep(random.uniform(0,0.05))

    pyautogui.keyDown(oppositeDirection)
    time.sleep(sleep_time_3)
    my_function.hold_key(my_common.key_map.health,hold_time=health_time)
    time.sleep(sleep_time_4)
    pyautogui.keyUp(oppositeDirection)
    time.sleep(sleep_time_5)

def how_should_i_do_inside(x,y,pixels): 
    if is_rune_on(pixels):
        solve_rune_on()
        return
    
    layer = which_layer_inside(y)
    match layer:
        case layer if layer > 4:
            i_am_NOT_near_greenHp_walk(my_common.direction.right)
        case 4:
            match x:
                case 48:
                    if Hp_precent(pixels) < 0.7:    
                        my_function.hold_key(my_common.key_map.health,hold_time=random.uniform(0.1,0.2))
                    if my_function.possible_true(0.4):
                        my_function.hold_key(my_common.direction.right,hold_time=random.uniform(0.4,0.6))
                        my_function.hold_key(my_common.key_map.angel,hold_time=random.uniform(0.1,0.2))
                        my_function.hold_key(my_common.direction.right,hold_time=random.uniform(0.8,1))
                        my_function.hold_key(my_common.key_map.ten,hold_time=random.uniform(0.1,0.2))
                    else:
                        my_function.hold_key(my_common.direction.right,my_common.key_map.flash,hold_time=random.uniform(0.1,0.2))   
                case x if x <= 66:
                    my_function.hold_key(my_common.direction.right,my_common.key_map.flash,hold_time=random.uniform(0.1,0.2))
                case _:
                    i_am_NOT_near_greenHp_walk(my_common.direction.right)
        case layer if 3 < layer < 4:
            i_am_NOT_near_greenHp_walk(my_common.direction.right)
        case 3:
            match x:
                case x if x >=57:
                    # if is_near_greenHpXY(x,y,pixels):
                    #     i_am_near_greenHp_flash(my_common.direction.left)
                    # else:
                    #     i_am_NOT_near_greenHp_flash(my_common.direction.left)
                    i_am_NOT_near_greenHp_flash(my_common.direction.left)
                case _:
                    if is_near_greenHpXY(x,y,pixels):
                        i_am_near_greenHp_walk(my_common.direction.left)
                    else:
                        i_am_NOT_near_greenHp_walk(my_common.direction.left)
        case layer if 2 < layer < 3:
            i_am_NOT_near_greenHp_walk(my_common.direction.left)
        case 2:
            match x:
                case x if x <= 66:
                    # if is_near_greenHpXY(x,y,pixels):
                    #     i_am_near_greenHp_flash(my_common.direction.right)
                    # else:
                    #     i_am_NOT_near_greenHp_flash(my_common.direction.right)
                    i_am_NOT_near_greenHp_flash(my_common.direction.right)
                case x if x < 80:
                    if is_near_greenHpXY(x,y,pixels):
                        i_am_near_greenHp_walk(my_common.direction.right)
                    else:
                        i_am_NOT_near_greenHp_walk(my_common.direction.right)
                case _ :
                    i_am_NOT_near_greenHp_walk(my_common.direction.left)
        case layer if 1 < layer < 2:
            i_am_NOT_near_greenHp_walk(my_common.direction.right)
        case 1:
            match x:
                case x if x >=57:
                    # if is_near_greenHpXY(x,y,pixels):
                    #     i_am_near_greenHp_flash(my_common.direction.left)
                    # else:
                    #     i_am_NOT_near_greenHp_flash(my_common.direction.left)
                    i_am_NOT_near_greenHp_flash(my_common.direction.left)
                case _:
                    if is_near_greenHpXY(x,y,pixels):
                        i_am_near_greenHp_walk(my_common.direction.left)
                    else:
                        i_am_NOT_near_greenHp_walk(my_common.direction.left)
        case layer if 0 < layer < 1:
            i_am_NOT_near_greenHp_walk(my_common.direction.left)
        case 0:
            match x:
                case x if x <= 91:
                    # if is_near_greenHpXY(x,y,pixels):
                    #     i_am_near_greenHp_flash(my_common.direction.right)
                    # else:
                    #     i_am_NOT_near_greenHp_flash(my_common.direction.right)
                    i_am_NOT_near_greenHp_flash(my_common.direction.right)
                case x if x > 91:
                    my_function.hold_key(my_common.direction.left,hold_time=0.2 )
                    my_function.hold_key(my_common.direction.up,hold_time=0.1)
                    my_function.hold_key(my_common.key_map.health,hold_time=0.1)
                    time.sleep(0.5)
        case layer if layer < 0:
            i_am_NOT_near_greenHp_walk(my_common.direction.right)
        case _:
            pass
    return  
    '''
    match y:
        case y if y < 160:
            routine_operation(health_or_not=False)
        case y if 160 <= y <= 161:  # layer_4
            match x:
                case x if x <= 48:
                    my_function.hold_key(my_common.key_map.health,hold_time=random.uniform(0.1,0.2))
                    routine_operation(walk_time=random.uniform(1,2),health_or_not=False)
                case _:
                    routine_operation(walk_time=random.uniform(1,2),health_or_not=False)
            return 4
        case y if 161 < y < 185:
            routine_operation()
        case y if 185 <= y <= 187:  # layer_3
            routine_operation(my_common.direction.left)
            return 3  
        case y if 187 < y < 201:
            routine_operation(my_common.direction.left)
        case y if 201 <= y <= 202:  # layer_2 
            match x:
                case x if x < 80:
                    routine_operation(my_common.direction.right)
                case _ :
                    routine_operation(my_common.direction.left)
            return 2
        case y if 202 < y < 221:
            routine_operation(my_common.direction.right)
        case y if 221 <= y <= 226:  # layer_1  
            routine_operation(my_common.direction.left)
            return 1  
        case y if 226 < y < 253:
            routine_operation(my_common.direction.left)
        case y if 253 <= y <= 259:
            match x:
                case x if x < 95:
                    routine_operation(my_common.direction.right)
                case _ :
                    screenshot = pyautogui.screenshot()
                    pixels = screenshot.load()
                    pixels_inside = find_yellow_in_smallMap_inside(pixels)
                    while True:
                        if my_function.interrupt_by_key():
                            break 
                        match pixels_inside:
                            case (x,y) if 89 <= x <= 91 :
                                my_function.enter_light()
                                break
                            case (x,y) if x < 89 :
                                my_function.hold_key(my_common.direction.right, hold_time=0.1)
                                screenshot = pyautogui.screenshot()
                                pixels = screenshot.load()
                                pixels_inside = find_yellow_in_smallMap_inside(pixels)
                            case (x,y) if x > 91 :
                                my_function.hold_key(my_common.direction.left, hold_time=0.1)
                                screenshot = pyautogui.screenshot()
                                pixels = screenshot.load()
                                pixels_inside = find_yellow_in_smallMap_inside(pixels)  
                            case _:
                                break
            return 0                        
        case _:
            my_function.hold_key(my_common.direction.right,my_common.direction.down,my_common.key_map.jump, hold_time=0.2)
            return None
        '''

def find_yellow_in_smallMap_outside(pixels) -> tuple | None:
    for y in range(30, 226):
        for x in range(0, 181):
            if pixels[x, y] == (255, 255, 136):
                return (x,y)
    return None

def find_yellow_in_smallMap_inside(pixels) -> tuple | None:
    for y in range(30, 290):
        for x in range(0, 137):
            if pixels[x, y] == (255, 255, 136):
                return (x,y)
    return None

def find_red_in_smallMap_inside(pixels) -> tuple | None:
    for y in range(30, 290):
        for x in range(0, 137):
            if pixels[x, y] == (255, 0, 0):
                return (x,y)
    return None

def find_greenHpXY(pixels) -> list[tuple[int,int]]:
    list_greenHpXYs = []
    for y in range(350,500): 
        for x in range(0,1280):
            if pixels[x, y] == (64, 204, 71):
                list_greenHpXYs.append((x,y))
    return list_greenHpXYs 

def is_near_greenHpXY(x,y,pixels):
    list_greenHpXYs = find_greenHpXY(pixels)
    realX = yellowX_mapping_realX(x)
    for greenHpXY in list_greenHpXYs:
        if (realX - 144) <= greenHpXY[0] <= (realX + 120):
            return True
    return False

# rune_test

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
        print(list_rune_test_edges_colors) 
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
            
def solve_rune_test():
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
                time.sleep(2)
            case "down":
                my_function.hold_key(my_common.direction.down,hold_time=0.1)
                time.sleep(2)
            case "left":
                my_function.hold_key(my_common.direction.left,hold_time=0.1)
                time.sleep(2)
            case "right":
                my_function.hold_key(my_common.direction.right,hold_time=0.1)
                time.sleep(2)
            case _:
                pass

# rune_test end

def solve_rune_on():    
    last_layer = 5
    last_XY = (0,0)
    while True:
        if my_function.interrupt_by_key():
            return
        screenshot = pyautogui.screenshot()
        pixels = screenshot.load()
        if find_red_in_smallMap_inside(pixels):
            change_channel()
            return
        if Hp_precent(pixels) < 0.5:
            my_function.hold_key(my_common.key_map.health,hold_time=random.uniform(0.5,0.7))
        if is_rune_test(pixels) is not None:
            solve_rune_test()
            return
        width, height = screenshot.size
        inside_pixel = am_i_inside(pixels)
        outside_pixel = am_i_outside(pixels)
        match (inside_pixel, outside_pixel):
            case ((x,y),None):
                now_layer = which_layer_inside(y)
                match now_layer:
                    case now_layer if now_layer > 4:
                        my_function.hold_key(my_common.direction.left,hold_time=2) 
                    case 4:
                        if last_layer != now_layer:
                            my_function.hold_key(my_common.direction.right,hold_time=0.5            )
                            my_function.hold_key(my_common.direction.up,hold_time=0.1)
                        elif last_XY == (x,y):
                            my_function.hold_key(my_common.direction.right,hold_time=0.1)
                            my_function.hold_key(my_common.direction.up,hold_time=0.1)
                            time.sleep(2)
                        else:
                            my_function.hold_key(my_common.direction.right,hold_time=0.1)
                            my_function.hold_key(my_common.direction.up,hold_time=0.1)
                    case now_layer if 3 < now_layer < 4:
                        my_function.hold_key(my_common.direction.right,hold_time=2)
                    case 3:
                        if last_layer != now_layer:
                            my_function.hold_key(my_common.direction.right,hold_time=2)
                            my_function.hold_key(my_common.direction.up,hold_time=0.1)
                        elif last_XY == (x,y):
                            my_function.hold_key(my_common.direction.left,hold_time=0.1)
                            my_function.hold_key(my_common.direction.up,hold_time=0.1)
                            time.sleep(2)
                        else:
                            my_function.hold_key(my_common.direction.left,hold_time=0.1)
                            my_function.hold_key(my_common.direction.up,hold_time=0.1)
                    case now_layer if 2 < now_layer < 3:
                        my_function.hold_key(my_common.direction.left,hold_time=2)
                    case 2:
                        if last_layer != now_layer:
                            my_function.hold_key(my_common.direction.left,hold_time=2)
                            my_function.hold_key(my_common.direction.up,hold_time=0.1)
                        elif last_XY == (x,y):
                            my_function.hold_key(my_common.direction.right,hold_time=0.1)
                            my_function.hold_key(my_common.direction.up,hold_time=0.1)
                            time.sleep(2)
                        else:
                            match x:
                                case x if x < 75:
                                    my_function.hold_key(my_common.direction.right,hold_time=0.1)
                                    my_function.hold_key(my_common.direction.up,hold_time=0.1)
                                case x if 75 <= x < 80:
                                    my_function.hold_key(my_common.key_map.flash,my_common.direction.right,hold_time=0.1)
                                    my_function.hold_key(my_common.direction.right,hold_time=2)
                                    my_function.hold_key(my_common.direction.up,hold_time=0.1)
                                case x if x >=80:
                                    my_function.hold_key(my_common.direction.left,hold_time=0.1)
                                    my_function.hold_key(my_common.direction.up,hold_time=0.1)
                    case now_layer if 1 < now_layer < 2:
                        my_function.hold_key(my_common.direction.right,hold_time=2)
                    case 1:
                        if last_layer != now_layer:
                            my_function.hold_key(my_common.direction.right,hold_time=2)
                            my_function.hold_key(my_common.direction.up,hold_time=0.1)
                        elif last_XY == (x,y):
                            my_function.hold_key(my_common.direction.left,hold_time=0.1)
                            my_function.hold_key(my_common.direction.up,hold_time=0.1)
                            time.sleep(2)
                        else:
                            my_function.hold_key(my_common.direction.left,hold_time=0.1)
                            my_function.hold_key(my_common.direction.up,hold_time=0.1)
                    case now_layer if 0 < now_layer < 1:
                        my_function.hold_key(my_common.direction.left,hold_time=2)
                    case 0:
                        if last_layer != now_layer:
                            my_function.hold_key(my_common.direction.left,hold_time=2)
                            my_function.hold_key(my_common.direction.up,hold_time=0.1)
                        elif last_XY == (x,y):
                            my_function.hold_key(my_common.direction.right,hold_time=0.1)
                            my_function.hold_key(my_common.direction.up,hold_time=0.1)
                            time.sleep(2)
                        else:
                            match x:
                                case x if x < 84:
                                    my_function.hold_key(my_common.direction.right,hold_time=0.1)
                                    my_function.hold_key(my_common.direction.up,hold_time=0.1)
                                case x if 84 <= x <= 90:
                                    my_function.hold_key(my_common.key_map.flash,my_common.direction.right,hold_time=0.1)
                                    my_function.hold_key(my_common.direction.right,hold_time=2)
                                    my_function.hold_key(my_common.direction.up,hold_time=0.1)
                                case x if x > 90:
                                    my_function.hold_key(my_common.direction.left,hold_time=0.1)
                                    my_function.hold_key(my_common.direction.up,hold_time=0.1)
                                case _:
                                    pass

                last_XY = (x,y)
                last_layer = now_layer
            case (None,(x,y)):
                return
            case _:
                time.sleep(1)
        # time.sleep(1) 
 

# -------------------------------------------------------------


time.sleep(0.5)
pyautogui.click(x=320, y=768)
time.sleep(0.5)

# ----------------------main---------------------------------------



not_inside_outside_count = 0
while True:
    if my_function.interrupt_by_key():
        break
    screenshot = pyautogui.screenshot()
    pixels = screenshot.load()
    width, height = screenshot.size
    inside_pixel = am_i_inside(pixels)
    outside_pixel = am_i_outside(pixels)
    # print((inside_pixel, outside_pixel))
    match (inside_pixel, outside_pixel):
        case ((x,y),None):
            not_inside_outside_count = 0
            if find_red_in_smallMap_inside(pixels) and which_layer_inside(y) == 4:
                change_channel()
            else:
                how_should_i_do_inside(x,y,pixels)
            # time.sleep(0.01)
        case (None,(x,y)):
            not_inside_outside_count = 0
            how_should_i_do_outside(x,y)
        case _:
            if not_inside_outside_count >= 10:
                not_inside_outside_count = 0
                change_channel()
                launch_game()
            else:
                not_inside_outside_count += 1
                time.sleep(1)


    
#---------------------test-------------------------------------

# screenshot = pyautogui.screenshot()
# pixels = screenshot.load()
# width, height = screenshot.size
# r = am_i_inside(pixels)
# my_function.hold_key(my_common.direction.up,hold_time=0.1)
# print(r)
# for i in range(10):
#     my_function.hold_key(my_common.direction.right,hold_time=0.1)
#     my_function.hold_key(my_common.direction.up,hold_time=0.1)
#     screenshot = pyautogui.screenshot()
#     pixels = screenshot.load()
#     width, height = screenshot.size
#     r = am_i_inside(pixels)
#     print(r)

# for i in range(1):
#     i_am_NOT_near_greenHp_walk(my_common.direction.right)
#     i_am_NOT_near_greenHp_walk(my_common.direction.left)







        
# -----------------------------------------------------------

time.sleep(0.5)
pyautogui.click(x=373, y=758)
time.sleep(0.5)

