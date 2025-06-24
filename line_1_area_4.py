import my_common
import my_function
import pyautogui
import random
import time


def hold_direction_and_sometime_health(
        direction:str = my_common.direction.right,
        total_walk_time:float = random.uniform(17,19),
    ):
    pyautogui.keyDown(direction)
    recent_walk_time = 0
    while recent_walk_time < total_walk_time:
        if my_function.interrupt_by_key():
            break
        
        walk_time:float = random.uniform(1.2,2.0) #
        health_time:float = random.uniform(0.1,0.9) #
        opposite = my_function.possible_true(0.1) #
        flash = my_function.possible_true(0.5) #
        jump = my_function.possible_true(0) #
        if flash:
            time.sleep(random.uniform(0.1,0.2))
            my_function.hold_key(my_common.key_map.flash, hold_time=random.uniform(0.1,0.2))
            my_function.hold_key(my_common.key_map.health,hold_time=random.uniform(0.1,0.2))
            time.sleep(random.uniform(0.1,0.2))
        if jump:
            
            my_function.hold_key(my_common.key_map.jump, hold_time=random.uniform(0.1,0.2))
            
        if opposite:
            pyautogui.keyUp(direction)
            recent_walk_time -= walk_time
            my_function.hold_key(my_function.opposite_direction(direction),hold_time=walk_time)
            time.sleep(random.uniform(0.1,0.2))
            pyautogui.keyDown(direction)
        else:
            recent_walk_time += walk_time
            time.sleep(walk_time)
        my_function.hold_key(my_common.key_map.health,hold_time=health_time)
    pyautogui.keyUp(direction)

# -----------------------------------



time.sleep(2)
pyautogui.keyDown(my_common.direction.up)
while True:
    if my_function.interrupt_by_key():
        break
    
    hold_direction_and_sometime_health(total_walk_time= random.uniform(18,20))
    hold_direction_and_sometime_health(direction=my_common.direction.left)
    my_function.hold_key("insert",hold_time=random.uniform(0.1,0.2))

pyautogui.keyUp(my_common.direction.up)
pyautogui.keyUp(my_common.direction.right)
pyautogui.keyUp(my_common.direction.left)




























"""
time.sleep(2)
while True:
    if keyboard.is_pressed('p'):
            break
    for _ in range(2):
        hold_key('right',1.5)
        hold_key(health)
    for _ in range(1):
        walk_flash_heath()






    for _ in range(17):
        if keyboard.is_pressed('p'):
            break
        up_flash()
        hold_key(health)
        hold_key("right",1.25)
        hold_key(health,0.1)
    
    for _ in range(2):
        hold_key('right',2)
        hold_key(health)

    for _ in range(20):
        if keyboard.is_pressed('p'):
            break
        hold_key("left",1.5)
        hold_key(health,0.1)
"""



