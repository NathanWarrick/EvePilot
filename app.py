import os
from time import sleep
from pynput.keyboard import Key, Controller

import src.plugins.ship as shp
import src.functions as fnc

curr_working_dir = os.getcwd()

keyboard = Controller()


def auto_compress(volume_max=10000, price_max=5000000):

    shp.inv_to_csv()
    inv = shp.inv_analyse()
    cost = int(inv[0])
    volume = int(inv[1])

    print("VOLUME")
    print("Volume set at: " + str(volume_max) + " m3")
    print("Current Volume: " + str(volume) + " m3")

    print("")

    print("PRICE")
    print("Price set at: " + str(price_max / 1000000) + " Millon ISK")
    print("Current Price: " + str(cost / 1000000) + " Millon ISK")

    print("")

    if cost >= price_max:
        print("Piloting back to station!")  # TODO Add piloting
        pass
    elif volume >= volume_max:
        for ore in shp.compression_ores():
            print("Currently compressing: " + ore + "\n")
            path = r"src\assets\ore\\" + ore + ".png"
            sleep(0.2)

            x, y = fnc.imagesearch(path, 0.95, 1)
            fnc.click_left(x, y)
            sleep(0.2)
            fnc.click_right(x, y)
            sleep(0.2)

            x, y = fnc.imagesearch(r"src\assets\compress.png", 0.95, 1)
            fnc.click_left(x, y)
            sleep(0.2)

            x, y = fnc.imagesearch(r"src\assets\compress_confirm.png", 0.95, 1)
            fnc.click_left(x, y)
            sleep(0.2)

            x, y = fnc.imagesearch(r"src\assets\compress_cancel.png", 0.95, 1)
            fnc.click_left(x, y)

            x, y = fnc.imagesearch(r"src\assets\stack_all.png", 0.95, 1)
            fnc.click_left(x, y)

            x, y = fnc.imagesearch(r"src\assets\my filters.png", 0.95, 1)
            fnc.click_left(x, y)

    else:
        print("No thresholds met, waiting...")
        print("\n\n\n")
        sleep(60)


def auto_compress_jet(volume_max=10000, price_max=5000000):

    shp.inv_to_csv()
    inv = shp.inv_analyse()
    cost = int(inv[0])
    volume = int(inv[1])

    print("VOLUME")
    print("Volume set at: " + str(volume_max) + " m3")
    print("Current Volume: " + str(volume) + " m3")

    print("")

    print("PRICE")
    print("Price set at: " + str(price_max / 1000000) + " Millon ISK")
    print("Current Price: " + str(cost / 1000000) + " Millon ISK")

    print("")

    if cost >= price_max:
        compressed_ores = shp.compressed_ores()
        if len(compressed_ores) > 0:
            print("Jetting Compressed Ore!")  # TODO Add piloting

            keyboard.press(Key.ctrl.value)
            sleep(0.2)

            for ore in compressed_ores:
                path = r"src\assets\ore\\" + ore + ".png"
                sleep(0.2)
                x, y = fnc.imagesearch(path, 0.95, 1)
                fnc.click_left(x, y)
                sleep(0.2)
            keyboard.release(Key.ctrl.value)
            sleep(0.2)
            x, y = fnc.imagesearch(
                r"src\assets\ore\\" + compressed_ores[0] + ".png", 0.95, 1
            )
            sleep(0.5)
            fnc.click_right(x, y)
            sleep(0.5)
            x, y = fnc.imagesearch(r"src\assets\jettison.png", 0.95, 1)
            sleep(0.5)
            fnc.click_left(x, y)
            sleep(0.5)

        else:
            print("Nothing to Compress")
    elif volume >= volume_max:
        for ore in shp.compression_ores():
            print("Currently compressing: " + ore + "\n")
            path = r"src\assets\ore\\" + ore + ".png"
            sleep(0.2)

            x, y = fnc.imagesearch(path, 0.95, 1)
            fnc.click_left(x, y)
            sleep(0.2)
            fnc.click_right(x, y)
            sleep(0.2)

            x, y = fnc.imagesearch(r"src\assets\compress.png", 0.95, 1)
            fnc.click_left(x, y)
            sleep(0.2)

            x, y = fnc.imagesearch(r"src\assets\compress_confirm.png", 0.95, 1)
            fnc.click_left(x, y)
            sleep(0.2)

            x, y = fnc.imagesearch(r"src\assets\compress_cancel.png", 0.95, 1)
            fnc.click_left(x, y)

            x, y = fnc.imagesearch(r"src\assets\stack_all.png", 0.95, 1)
            fnc.click_left(x, y)

            x, y = fnc.imagesearch(r"src\assets\my filters.png", 0.95, 1)
            fnc.click_left(x, y)

    else:
        print("No thresholds met, waiting...")
        print("\n\n\n")
        sleep(60)


done = False
while done != True:
    auto_compress_jet(3500, 5000000)
