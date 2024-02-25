import os
from time import sleep

import src.plugins.ship as shp
import src.functions as fnc

curr_working_dir = os.getcwd()


def auto_compress(volume_max=10000, price_max=5000000):

    shp.inv_to_csv()
    inv = shp.inv_analyse("*")
    cost = int(inv[0])
    volume = int(inv[1])

    print("VOLUME")
    print("Volume set at: " + str(volume_max) + " m3")
    print("Current Volume:" + str(volume) + " m3")

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
            print("Currently compressing: " + ore)
            path = r"src\assets\ore\\" + ore + ".png"

            x, y = fnc.imagesearch(path, 0.95)
            fnc.click_left(x, y)
            sleep(0.2)
            fnc.click_right(x, y)
            sleep(0.2)

            x, y = fnc.imagesearch(r"src\assets\compress.png", 0.95)
            fnc.click_left(x, y)
            sleep(0.2)

            x, y = fnc.imagesearch(r"src\assets\compress_confirm.png", 0.95)
            fnc.click_left(x, y)
            sleep(0.2)

            x, y = fnc.imagesearch(r"src\assets\compress_cancel.png", 0.95)
            fnc.click_left(x, y)

            x, y = fnc.imagesearch(r"src\assets\stack_all.png", 0.95)
            fnc.click_left(x, y)

            x, y = fnc.imagesearch(r"src\assets\my filters.png", 0.95)
            fnc.click_left(x, y)

    else:
        print("No thresholds met, waiting...")
        print("\n\n\n")
        sleep(60)


# done = False
# while done != True:
#     auto_compress(20000, 1000000000)
