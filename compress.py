import functions as fnc
from time import sleep
import win32api, win32con


def click_left(x, y):
    win32api.SetCursorPos((int(x), int(y)))
    sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def click_right(x, y):
    win32api.SetCursorPos((int(x), int(y)))
    sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
    sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)


while None != 0:
    if fnc.imagesearch(r"src\assets\ore\Brimful_Bitumens.png") != [-1, -1]:
        print("Compressing!")
        x, y = fnc.imagesearch(r"src\assets\ore\Brimful_Bitumens.png")
        fnc.click_right(int(x), int(y - 40))
        sleep(1)
        fnc.click_right(int(x), int(y - 40))
        sleep(1)

        x, y = fnc.imagesearch(r"src\assets\compress.png")
        click_left(x, y)
        sleep(2)

        x, y = fnc.imagesearch(r"src\assets\compress_confirm.png")
        click_left(x, y)
        sleep(2)

        x, y = fnc.imagesearch(r"src\assets\compress_cancel.png")
        click_left(x, y)
        sleep(2)

        x, y = fnc.imagesearch(r"src\assets\ore\Compressed_Brimful_Bitumens.png")
        fnc.click_right(int(x), int(y))
        sleep(1)
        fnc.click_right(int(x), int(y))
        sleep(1)

        x, y = fnc.imagesearch(r"src\assets\stack_all.png", 0.95)
        click_left(x, y)
        sleep(2)

    else:
        print("Not Found")
        sleep(60)
