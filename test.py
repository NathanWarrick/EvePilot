import src.functions as fnc

x, y = fnc.imagesearch(r"src\assets\stack_all.png", 0.90, 1)
fnc.click_left(x, int(y + 60))
