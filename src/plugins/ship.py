import src.functions as fnc
from time import sleep
import win32api, mss
from PIL import Image
import cv2
import numpy as np
from pynput.keyboard import Key, Controller
import pandas as pd

import src.functions as fnc
import src.var as info

keyboard = Controller()


def inv_to_csv():
    """Read contents of ore hold and export to '/src/assets/temp/inv.csv' \n
    Call before making inventory related calculations"""

    # Select all and stack, and copy to clipboard
    # try:
    #     fnc.imagesearch(r"src\assets\stack_all.png", 0.99)
    #     print("Found")
    # except:
    #     print("Image not found")
    x, y = fnc.imagesearch(r"src\assets\stack_all.png", 0.90, 1)
    fnc.click_left(x, y)
    sleep(0.1)
    keyboard.press(Key.ctrl.value)
    sleep(0.1)
    keyboard.type("a")
    sleep(0.1)
    keyboard.type("c")
    sleep(0.1)
    keyboard.release(Key.ctrl.value)
    sleep(0.5)
    x, y = fnc.imagesearch(r"src\assets\stack_all.png", 0.90, 1)
    fnc.click_left(x, int(y - 35))

    # Read from clipboard into a pd dataframe
    df_hold = pd.read_clipboard(
        sep="\t", names=["Name", "Quantity", "Group", "Size", "Slot", "Volume", "Price"]
    )

    # Clean up the dataframe
    df_hold = df_hold.replace(" ISK", "", regex=True)
    df_hold = df_hold.replace(",", "", regex=True)
    df_hold = df_hold.replace(" m3", "", regex=True)

    # Export Dataframe to csv
    df_hold.to_csv(r"src/assets/temp/inv.csv")
    # print("Inventory Exported")


def hold_full():
    """Determined how full the ore hold is by reading the bar in the inventory hold

    :return: returns a percentage as an integer
    :rtype: int
    """
    x, y = fnc.imagesearch(r"src\assets\stack_all.png", 0.95, 1)
    x_search, y_search = fnc.imagesearch(r"src\assets\search.png", 0.95, 1)
    # Reverse coordinate correction
    x = x - win32api.GetSystemMetrics(76)
    y = y - win32api.GetSystemMetrics(77)
    x_search = x_search - win32api.GetSystemMetrics(76)
    y_search = y_search - win32api.GetSystemMetrics(77)

    with mss.mss() as sct:
        x_offset = x + 44
        y_offset = y - 11
        width = x_search - x - 111
        height = 1

        sct_img = sct.grab(sct.monitors[0])
        img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
        im = img.crop((x_offset, y_offset, x_offset + width, y_offset + height))
        im.save(r"src/assets/temp/inv.png")

        im_gray = cv2.imread(r"src/assets/temp/inv.png", cv2.IMREAD_GRAYSCALE)
        thresh = 68
        im_bw = cv2.threshold(im_gray, thresh, 255, cv2.THRESH_BINARY)[1]
        cv2.imwrite(r"src/assets/temp/inv_bw.png", im_bw)

        total_area = np.sum(im_bw == 255) + np.sum(im_bw == 0)
        percent_full = np.sum(im_bw == 255) / total_area
        percent_full = int(percent_full * 100)
    return percent_full


def inv_analyse(
    search="*",
):  # TODO Use to go home if compressed ore reaches a certain number
    """Returns the total cost and volume. \n
    Call inv_to_csv() for the most up to date information

    :return: Cost, Volume
    :rtype: Tupple
    """
    df = pd.read_csv(r"src/assets/temp/inv.csv", index_col=0)
    if search != "*":
        contain_values = df[df["Name"].str.contains(search)]
        cost = contain_values["Price"].sum()
        volume = contain_values["Volume"].sum()
    else:
        cost = df["Price"].sum()
        volume = df["Volume"].sum()
    return cost, volume


def compression_ores():
    """Retuns ores avaliable for compression \n
    Call inv_to_csv() for the most up to date information

    :return: Compressible Ores
    :rtype: List
    """
    hold_ore = []
    df = pd.read_csv(r"src/assets/temp/inv.csv", index_col=0)
    for ore in info.moon_ores:
        if df["Name"].eq(ore).any():
            hold_ore.append(ore)
    return hold_ore


def compressed_ores():
    """Retuns ores that have been compressed \n
    Call inv_to_csv() for the most up to date information

    :return: Compressed Ores
    :rtype: List
    """

    # df = pd.read_csv(r"src/assets/temp/inv.csv", index_col=0)
    # contain_values = df[df["Name"].str.contains("Compressed")]
    # return contain_values

    hold_ore = []
    df = pd.read_csv(r"src/assets/temp/inv.csv", index_col=0)
    for ore in info.compressed_ores:
        if df["Name"].eq(ore).any():
            hold_ore.append(ore)
    return hold_ore
