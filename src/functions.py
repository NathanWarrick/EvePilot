import csv, os, mss, cv2, pynput, time, win32api, win32con
import numpy as np
import win32gui
import re
import random
from time import sleep

keyboard = pynput.keyboard.Controller()
curr_working_dir = os.getcwd()

# Virtual Screen Measurements
xmin = win32api.GetSystemMetrics(76)
xmax = win32api.GetSystemMetrics(78)

ymin = win32api.GetSystemMetrics(77)
ymax = win32api.GetSystemMetrics(79)


def click_left(x, y):
    if x is not None and y is not None:
        x = int(x)
        y = int(y)
        win32api.SetCursorPos((x, y))
        sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    else:
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def drag_left(x_start, y_start, x_end, y_end):

    x_start = int(x_start)
    y_start = int(y_start)
    x_end = int(x_end)
    y_end = int(y_end)

    win32api.SetCursorPos((x_start, y_start))
    sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x_start, y_start, 0, 0)
    sleep(0.2)
    win32api.SetCursorPos((x_end, y_end))
    sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x_end, y_end, 0, 0)


def click_right(x, y):
    if x is not None and y is not None:
        x = int(x)
        y = int(y)
        win32api.SetCursorPos((x, y))
        sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, x, y, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, x, y, 0, 0)
    else:
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)


def kbd_type(text: str):
    """Use pynput to enter text

    :param text: Text to enter on keyboard
    :type text: str
    """
    keyboard.type(text)


def moveto(image: str, confidence=0.9, wait=0.1):
    found = False
    i = 0
    while found == False:
        if i == 30:
            raise RuntimeError("Unable to find image in the 30 second window")
        coordds = imagesearch(image, confidence=confidence)
        i += 1
        time.sleep(1)
        if coordds != [-1, -1]:
            found = True
            win32api.SetCursorPos((int(coordds[0]), int(coordds[1])))


def clickon(image: str, confidence=0.9, clicktype="left", wait=0.1):
    found = False
    i = 0
    while found == False:
        if i > 1:
            xrandom = random.randint(int(xmin), int(xmax))
            yrandom = random.randint(int(ymin), int(ymax))
            win32api.SetCursorPos((int(xrandom), int(yrandom)))
        coordds = imagesearch(image, confidence=confidence)
        i += 1
        time.sleep(1)

        if i == 10:
            raise RuntimeError("Unable to find image in the 10 second window")

        if coordds != [-1, -1]:
            found = True
            if clicktype == "left":
                click_left(int(coordds[0]), int(coordds[1]))
            elif clicktype == "right":
                click_right(int(coordds[0]), int(coordds[1]))
            elif clicktype == "none":
                continue
            time.sleep(wait)


def imagesearch(image: str, confidence=0.9, screen=0):
    with mss.mss() as sct:
        im = sct.grab(sct.monitors[screen])
        img_rgb = np.array(im)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        template = cv2.imread(image, 0)
        if template is None:
            raise FileNotFoundError("Image file not found: {}".format(image))
        template.shape[::-1]

        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        print(max_val)
        if max_val < confidence:
            return [-1, -1]

        # Do some math to calculate the middle of the image
        templatesize = tuple(
            ti / 2 for ti in template.shape
        )  # Find the size of the template image and divide by 2

        # Convert H/W to W/H
        templatesize = list(templatesize)
        templatesize[0], templatesize[1] = templatesize[1], templatesize[0]

        # Calculate the middle of the image
        x, y = tuple(
            map(lambda i, j: i + j, max_loc, templatesize)
        )  # Add the best match to half the image size to find the middle

    if screen == 0:
        x = x + win32api.GetSystemMetrics(76)
        y = y + win32api.GetSystemMetrics(77)

    return x, y


def imagecheck(image: str):
    """Continues to try to load an image until it successfully loads

    :param image: path to image to search for
    :type image: str
    """
    load = False
    i = 0
    while load == False:
        if imagesearch(image) == [-1, -1]:
            load == False
            print("[INFO] " + image + " not found")
            i = i + 1
            time.sleep(1)
        else:
            load == True
            print("[INFO] " + image + " found")
            break
