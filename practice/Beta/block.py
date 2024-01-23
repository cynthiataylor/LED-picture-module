import picture
# from picture import *
import random
import time
import sys

picture.new_picture(int(sys.argv[1]),int(sys.argv[1]))
picture.set_fill_color("black")
picture.draw_filled_rectangle(0,0,int(sys.argv[1]),int(sys.argv[1]))

red = 255
green = 200
blue = 23

y = 0
x = 0
positions = []
counter = 0
while True:
    for t in range(4):
        h = random.randint(20,int(sys.argv[1]))
        x+= h

        picture.set_fill_color(red,green,blue)
        # if counter % 4 == 0 or counter % 3 == 0:
        picture.draw_filled_square(x,y,int(sys.argv[3]))

        x = t * 50
        counter += 1
        if x >= int(sys.argv[1])//4:
            x = 0
            y += 50
        if y >= int(sys.argv[1])//2:
            y = int(sys.argv[1])//3
            x = 0
            x += 100
            y = 0
            x = 800
            x = 0

        print(counter)
        # picture.set_fill_color("black")
        # pictures.draw_filled_rectangle(0,0,int(sys.argv[1]),int(sys.argv[1]))


        # pictures.display()
        # picture.draw_on_matrix()


        blue = (blue - 3 * t) % 255 
        green = (green + y) % 255
        green = (green //(x + 1))%255
        # print(positions)
        
        time.sleep(int(sys.argv[2]))

