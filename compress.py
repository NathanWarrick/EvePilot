import functions as fnc
from time import sleep
import win32api, win32con, mss
from PIL import Image
import cv2
import numpy as np
from pynput.keyboard import Key, Controller
import win32clipboard
import pandas as pd

keyboard = Controller()


def click_left(x, y):
    win32api.SetCursorPos((int(x), int(y)))
    sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def click_right(x, y):
    win32api.SetCursorPos((int(x), int(y)))
    sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)


def hold_full():
    x, y = fnc.imagesearch(r"src\assets\stack_all.png", 0.95)
    # Reverse coordinate correction
    x = x - win32api.GetSystemMetrics(76)
    y = y - win32api.GetSystemMetrics(77)
    # print(x, y)

    with mss.mss() as sct:
        x_offset = x + 68
        y_offset = y - 11
        width = 209
        height = 8

        sct_img = sct.grab(sct.monitors[0])
        img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
        im = img.crop((x_offset, y_offset, x_offset + width, y_offset + height))
        im.save(r"src/assets/temp/inv.png")

        im_gray = cv2.imread(r"src/assets/temp/inv.png", cv2.IMREAD_GRAYSCALE)
        thresh = 68
        im_bw = cv2.threshold(im_gray, thresh, 255, cv2.THRESH_BINARY)[1]
        cv2.imwrite(r"src/assets/temp/inv_bw.png", im_bw)

        percent_full = np.sum(im_bw == 255) / 1664
        percent_full = int(percent_full * 100)
    return percent_full


def inv_to_csv():
    x, y = fnc.imagesearch(r"src\assets\stack_all.png", 0.90)
    fnc.click_left(x, y)
    sleep(0.1)
    keyboard.press(Key.ctrl.value)
    sleep(0.1)
    keyboard.type("a")
    sleep(0.1)
    keyboard.type("c")
    sleep(0.1)
    keyboard.release(Key.ctrl.value)

    df_hold = pd.read_clipboard(
        sep="\t", names=["Name", "Quantity", "Group", "Size", "Slot", "Volume", "Price"]
    )

    # Clean up the dataframe
    df_hold = df_hold.replace(" ISK", "", regex=True)
    df_hold = df_hold.replace(",", "", regex=True)
    df_hold = df_hold.replace(" m3", "", regex=True)

    df_hold.to_csv(r"src/assets/temp/inv.csv")
    return df_hold


def main():

    while None != 0:
        if hold_full() > 50:
            if fnc.imagesearch(r"src\assets\ore\Brimful_Bitumens.png") != [-1, -1]:
                print("Compressing!")
                x, y = fnc.imagesearch(r"src\assets\ore\Brimful_Bitumens.png", 0.95)
                click_right(x, y)
                sleep(0.2)

                x, y = fnc.imagesearch(r"src\assets\compress.png", 0.95)
                click_left(x, y)
                sleep(0.2)

                x, y = fnc.imagesearch(r"src\assets\compress_confirm.png", 0.95)
                click_left(x, y)
                sleep(0.2)

                x, y = fnc.imagesearch(r"src\assets\compress_cancel.png", 0.95)
                click_left(x, y)

                x, y = fnc.imagesearch(r"src\assets\stack_all.png", 0.95)
                click_left(x, y)
        else:
            print("You have only used " + str(hold_full()) + "%")
            sleep(60)


main()
# print(inv_to_csv())
