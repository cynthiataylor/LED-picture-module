import picture
import sys
from time import sleep
import random

def circle(width,height):

    picture.new_picture(width, height)  # Create a new picture
    picture.set_fill_color("black")     # Set the fill color after creating the new picture
    picture.draw_filled_rectangle(0, 0, width, height)

    #variablesf
    radius = 4
    size = 2
    color = [(107, 176, 126), (186, 71, 71), (55, 148, 191), (171, 84, 171), (58, 156, 12), (196, 137, 47)]
    color_index = 0
    rand_x = random.randrange(15, 55)
    rand_y = random.randrange(30, 95)

    computer = sys.argv[-1]
    while True: 
        
        if color_index == 6:
            color_index = 0

        picture.set_outline_color(color[color_index])

        #pen width
        if size == 6:
            size = 1    
            picture.set_pen_width(size)
        size += 1
        picture.draw_circle(rand_x, rand_y,radius)
        sleep(0.05)

        radius += 4

        # Matrix or Laptop
        if computer == "L":
            picture.display()
        elif computer == "D":
            picture.draw_on_matrix()

        # Maximum radius
        if radius == 24:
            radius = 4
            color_index += 1
            rand_x = random.randrange(15, 55)
            rand_y = random.randrange(15, 55)
            picture.set_fill_color("black")
            picture.set_outline_color("black")
            picture.draw_filled_rectangle(0,0,width,height)


width = int(sys.argv[1])
height = int(sys.argv[1])

circle(width,height)