from folders import importing_library_picture_from_scroll_folder

importing_library_picture_from_scroll_folder() # to avoid repetition of files in the same folder

from Module.picture import *


# from picture import *
from folders import importing_library_picture_from_scroll_folder

importing_library_picture_from_scroll_folder() # to avoid repetition of files in the same folder

from Module.picture import *


# from picture import *
import random
import time

new_picture(800,400)
set_fill_color("black")
draw_filled_rectangle(0,0,800,400)

red = 255
green = 200
blue = 23

y = 0
x = 0
positions = []
counter = 0
while True:
    for t in range(4):
        h = random.randint(20,400)
        x+= h

        set_fill_color(red,green,blue)
        if counter % 4 == 0 or counter % 3 == 0:
            draw_filled_square(x,y,50)

        x = t * 50
        counter += 1
        if x >= 150:
            x = 0
            y += 50
        if y >= 300:
            y = 400
            x = 0
            x += 100
            y = 0
            x = 800
            x = 0

        print(counter)
        if counter %10 == 0:
            set_fill_color("black")
            draw_filled_rectangle(0,0,800,400)


        display()

        blue = (blue - 3 * t) % 255 
        green = (green + y) % 255
        green = (green //(x + 1))%255
        # print(positions)

