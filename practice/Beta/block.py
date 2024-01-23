import picture
# from picture import *
import random
import time

picture.new_picture(800,400)
picture.set_fill_color("black")
picture.draw_filled_rectangle(0,0,800,400)

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

        picture.set_fill_color(red,green,blue)
        if counter % 4 == 0 or counter % 3 == 0:
            picture.draw_filled_square(x,y,50)

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
        # picture.set_fill_color("black")
        picture.draw_filled_rectangle(0,0,800,400)


        # picture.display()
        picture.draw_on_matrix()

        blue = (blue - 3 * t) % 255 
        green = (green + y) % 255
        green = (green //(x + 1))%255
        # print(positions)

