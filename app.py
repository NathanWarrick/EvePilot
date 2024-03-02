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
        for ore in shp.compressible_ores():
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
        for ore in shp.compressible_ores():
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


def auto_move(volume_max=5000, compression=False, Jet=False):
    """Automatically moves ore into a nearby Orca's Fleet Hangar, or Jettisons it"""

    shp.inv_to_csv()
    inv = shp.inv_analyse()
    volume = int(inv[0])
    cost = int(inv[1])

    print("\nVOLUME")
    print("Volume set at: " + str(volume_max) + " m3")
    print("Current Volume: " + str(volume) + " m3")

    print("")

    # print("PRICE")
    # print("Price set at: " + str(price_max / 1000000) + " Millon ISK")
    # print("Current Price: " + str(cost / 1000000) + " Millon ISK")

    print("")

    move = False
    compress = False

    compressible_ores = shp.compressible_ores()[0]
    compressible_ores_cost = shp.compressible_ores()[1]
    compressed_ores = shp.compressed_ores()[0]
    compressed_ores_cost = shp.compressed_ores()[1]

    if volume >= volume_max and Jet == False:
        print("You're running out of space! \n")
        if (
            compression == True and compressible_ores != []
        ):  # Compress Raw Ore if enabled
            print("Compressing Ore!")
            for ore in compressible_ores:
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
        elif (
            compression == False and compressible_ores != []
        ):  # Move compressible ores to orca if compression is off
            print("Moving Uncompressed Ore to Orca!")  # TODO Add piloting
            sleep(0.2)

            for ore in compressible_ores:
                path = r"src\assets\ore\\" + ore + ".png"
                sleep(0.2)

                x, y = fnc.imagesearch(path, 0.95, 1)
                orca_x, orca_y = fnc.imagesearch(
                    r"src\assets\orca_fleet_hangar.png", 0.95, 1
                )
                fnc.click_left(x, y)
                sleep(0.2)
                fnc.drag_left(x, y, orca_x, orca_y)
                sleep(0.2)

        if compressed_ores != []:  # Move Compressed Ores to Orca
            for ore in compressed_ores:
                path = r"src\assets\ore\\" + ore + ".png"
                sleep(0.2)

                x, y = fnc.imagesearch(path, 0.95, 1)
                orca_x, orca_y = fnc.imagesearch(
                    r"src\assets\orca_fleet_hangar.png", 0.95, 1
                )
                fnc.click_left(x, y)
                sleep(0.2)
                fnc.drag_left(x, y, orca_x, orca_y)
                sleep(0.2)

    elif volume >= volume_max and Jet == True:
        print("Jetting All Ore!")  # TODO Add piloting
        x, y = fnc.imagesearch(r"src\assets\stack_all.png", 0.90, 1)
        fnc.click_left(x, y)
        sleep(0.1)
        keyboard.press(Key.ctrl.value)
        sleep(0.1)
        keyboard.type("a")
        sleep(0.1)
        keyboard.release(Key.ctrl.value)
        sleep(0.5)
        x, y = fnc.imagesearch(r"src\assets\stack_all.png", 0.90, 1)
        fnc.click_right(x, int(y + 60))
        sleep(0.5)
        x, y = fnc.imagesearch(r"src\assets\jettison.png", 0.95, 1)
        sleep(0.5)
        fnc.click_left(x, y)
        sleep(0.5)

    else:
        print("No thresholds met, waiting...")
        print("\n\n\n")


done = False
while done != True:
    auto_move(6000, False, True)
    sleep(100)  # Run routine every 100 seconds
