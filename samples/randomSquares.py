

import picture as picture
import random
import time
import sys

picture.new_picture(128,128)
picture.set_fill_color("black")
picture.draw_filled_rectangle(0,0,128,128)


red = 255
green = 200
blue = 45


x = 0
y = 0
positions = []

count = 0

def snake(width):
    picture.set_fill_color("white")
    picture.set_pen_width(3)
    picture.draw_filled_rectangle(0,0,64,64)
    for i in range(width):
        picture.draw_forward(20 + i)
        #picture.rotate(120)
        picture.draw_on_matrix()
 
while x < 500:
    picture.set_fill_color(red,green,blue)
    y = random.randint(4,128)
    count += 1
    x += 1
    positions.append((x,y))
    
    if x >=128:
        x = 10
        if count % 4 == 0:
            x = 0
        elif count % 9 == 0:
            y += 2
        picture.set_fill_color('black')
        picture.draw_filled_rectangle(0,0,128,128)

    picture.draw_filled_square((x) * ((128-20)/12),y,10)

         
    red = (red - 20) % 250
    blue = (blue - 20) % 250
    green = (blue + 20) % 255

    picture.draw_on_matrix()
    time.sleep(0)


