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

    computer = sys.argv[-1]
    while True:
        picture.set_outline_color(red ,green, blue)
        picture.set_pen_width(size)
        size += 1
        picture.draw_circle(width //2,height // 2,radius)
        if size ==8:
            size = 4
        radius += 2

        if computer == "L":
            picture.display()
        elif computer == "D":
            picture.draw_on_matrix()
            time.sleep(float(sys.argv[2]))

        if radius >= 40:
            radius = 4
            picture.set_fill_color("black")
            picture.set_outline_color("black")
            picture.draw_filled_rectangle(0,0,width,height)
            
    

        red = (red - 20) % 250
        blue = (blue - 20) % 250
        green = (blue + 20) % 255

width = int(sys.argv[1])
height = int(sys.argv[1])

circle(width,height)
