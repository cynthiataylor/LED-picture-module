
import picture
import sys
import time
def circle(width,height):

    picture.new_picture(width,height)
    picture.set_fill_color("black")

    red = 255
    green = 200
    blue = 45

    radius = 2
    size = 2

    computer = "D"

    runtime = 800
    while runtime >=0:
        runtime -=1
        picture.set_outline_color(red ,green, blue)
        picture.set_pen_width(size)
        size += 1
        picture.draw_circle(width //2,height // 2,radius)
        if size ==8:
            size = 2
        radius += 1

        picture.draw_on_matrix()
        time.sleep(0.02)

        if radius >= 100:
            radius = 1
            picture.set_fill_color("black")
            picture.set_outline_color("black")
            picture.draw_filled_rectangle(0,0,width,height)
            
    

        red = (red - 20) % 250
        blue = (blue - 20) % 250
        green = (blue + 20) % 255

width = 128
height = 128

circle(width,height)
