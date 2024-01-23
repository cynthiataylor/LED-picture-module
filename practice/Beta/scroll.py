from folders import importing_library_picture_from_scroll_folder

importing_library_picture_from_scroll_folder() # to avoid repetition of files in the same folder

from Module.picture import *


from picture import *
import random
import time

new_picture(128,128)
set_fill_color("black")
draw_filled_rectangle(0,0,128,128)


# set_outline_color("white")
# set_pen_width(2)

red = 255
green = 200
blue = 45

x = 0
y = 0
positions = []

count = 0
while x < 1000:
    # for k in range(7):
    set_fill_color(red,green,blue)
    y = random.randint(4,128)
    count += 1
    x += 1
    positions.append((x,y))
    # print(x)
    
    if x == 15:
        x = 10
        if count % 4 == 0:
            x = 0
        elif count % 9 == 0:
            y += 2
        set_fill_color('black')
        draw_filled_rectangle(0,0,800,800)

    draw_filled_square((x) * (600/12),y,50)
    print(((x) * (600//12),y))
        
    red = (red - 20) % 250
    blue = (blue - 20) % 250
    green = (blue + 20) % 255


    # display()
    draw_on_matrix()
    # time.sleep(1)

    


