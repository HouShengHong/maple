import pyautogui
import keyboard
import time
import random
import my_common

def opposite_direction(direction:str = my_common.direction.right):
    match direction:
        case my_common.direction.left:
            return my_common.direction.right
        case my_common.direction.up:
            return my_common.direction.down
        case my_common.direction.down:
            return my_common.direction.up
        case _ :
            return my_common.direction.left

def possible_true(probability:int|float = 0) -> bool:
    return random.random() < probability

def interrupt_by_key(key:str = my_common.key_map.interrupt) -> bool:
    if keyboard.is_pressed(key):
        return True
    else:
        return False

def hold_key(*keys, hold_time = 0) -> None:
    for i in keys:
        pyautogui.keyDown(i)
    time.sleep(hold_time)
    for i in keys[::-1]:
        pyautogui.keyUp(i)

def enter_light(time_sleep = 1) -> None:
    hold_key(my_common.direction.up, hold_time=0.05)
    pyautogui.keyUp(my_common.direction.up)
    time.sleep(time_sleep)

def walk_flash_walk_jump_walk_health_walk(
        direction:str = my_common.direction.right,
        walk_time_1:int|float = 0,

        flash_or_no:bool = False,
        flash_time:int|float = 0,

        walk_time_2:int|float = 0,

        jump_or_no:bool = False,
        jump_time:int|float = 0,

        walk_time_3:int|float = 0,
        health_or_no:bool = True,
        health_time:int|float = 0,

        walk_time_4:int|float = 0
    ) -> None:
    
    pyautogui.keyDown(direction)
    time.sleep(walk_time_1) #walk_1

    if flash_or_no: #flash
        hold_key(my_common.key_map.flash, hold_time=flash_time)
    
    time.sleep(walk_time_2) #walk_2

    if jump_or_no: #jump
        hold_key(my_common.key_map.jump, hold_time=jump_time)
    
    time.sleep(walk_time_3) #walk_3

    if health_or_no: #health
        hold_key(my_common.key_map.health, hold_time=health_time)
    
    time.sleep(walk_time_4) #walk_4
    pyautogui.keyUp(direction)

if __name__ == "__main__":
    pass

