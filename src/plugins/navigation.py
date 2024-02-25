from time import sleep
from pynput.keyboard import Key, Controller

import src.functions as fnc

keyboard = Controller()


def search(location):
    print("Searching for: " + str(location))
    x, y = fnc.imagesearch(r"src\assets\stack_all.png", 0.95)
    fnc.click_left(x, y)
    keyboard.press(Key.shift.value)
    sleep(0.1)
    keyboard.type("s")
    sleep(0.1)
    keyboard.release(Key.shift.value)
    sleep(0.5)
    keyboard.type(location)
    sleep(0.1)
    keyboard.press(Key.enter.value)
    keyboard.release(Key.enter.value)
    sleep(5)
    x, y = fnc.imagesearch(r"src\assets\structures.png", 0.90)
    fnc.click_right(x, int(y + 20))
    sleep(0.2)
    try:
        x, y = fnc.imagesearch(r"src\assets\set_destination.png", 1)
        fnc.click_left(x, y)
    except:
        print("Is this already your destination?")
        return
    sleep(0.2)
    keyboard.press(Key.ctrl.value)
    sleep(0.1)
    keyboard.type("s")
    sleep(0.1)
    keyboard.release(Key.ctrl.value)
    x, y = fnc.imagesearch(r"src\assets\close.png", 0.95)
    fnc.click_left(x, y)
