import picture
import time

picture.new_picture(600,600)
picture.set_fill_color("black")
picture.draw_filled_rectangle(0,0,600,600)
size = 1
red = 205
green = 20
blue = 10
size = 2
i = 1
picture.set_position(300,300)
while True:
    picture.set_pen_width(size)
    # picture.set_fill_color()
    picture.set_outline_color(red,green,blue)
    picture.draw_forward(i)
    i += 1
    picture.rotate(45)
    picture.draw_forward(-i//3)
    picture.display()
    time.sleep(0)
    red = (red - 2) % 250
    blue = (blue - 20) % 250
    green = (blue + 20) % 255