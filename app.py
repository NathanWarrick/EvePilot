import os
from time import sleep

import src.plugins.ship as shp
import src.functions as fnc

curr_working_dir = os.getcwd()

# shp.inv_to_csv()


def main(thresh):

    while None != 0:
        if shp.hold_full() >= thresh:
            hold_ore = shp.compression_ores()
            for ore in hold_ore:
                print("Compressing " + ore)
                ore_string = r"src\assets\ore\\" + ore + ".png"

                x, y = fnc.imagesearch(ore_string, 0.95)
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
        print("You have only used " + str(shp.hold_full()) + "%")
        sleep(30)


main(50)
