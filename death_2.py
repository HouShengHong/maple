import my_common
import my_function
import pyautogui
import random
import time


def hold_direction_and_sometime_health(
        direction:str = my_common.direction.right,
        total_walk_time:float = random.uniform(17,20),
    ):
    pyautogui.keyDown(direction)
    recent_walk_time = 0
    while recent_walk_time < total_walk_time:
        if my_function.interrupt_by_key():
            break
        
        walk_time:float = random.uniform(0.6,1.8) #
        health_time:float = random.uniform(0.1,0.8) #
        opposite = my_function.possible_true(0.15) #
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
    
    hold_direction_and_sometime_health()
    hold_direction_and_sometime_health(my_common.direction.left,random.uniform(15,17))
    my_function.hold_key("insert",hold_time=random.uniform(0.1,0.2))

pyautogui.keyUp(my_common.direction.up)
pyautogui.keyUp(my_common.direction.right)
pyautogui.keyUp(my_common.direction.left)

