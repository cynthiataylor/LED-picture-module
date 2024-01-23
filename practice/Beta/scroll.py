

import picture
import random
import time
import sys

picture.new_picture(int(sys.argv[1]),int(sys.argv[1]))
picture.set_fill_color("black")
picture.draw_filled_rectangle(0,0,int(sys.argv[1]),int(sys.argv[1]))


red = 255
green = 200
blue = 45

x = 0
y = 0
positions = []

count = 0
while x < 1000:
    # for k in range(7):
    picture.set_fill_color(red,green,blue)
    y = random.randint(4,int(sys.argv[1]))
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
        picture.set_fill_color('black')
        picture.draw_filled_rectangle(0,0,int(sys.argv[1]),int(sys.argv[1]))

    picture.draw_filled_square((x) * ((int(sys.argv[1])-20)/12),y,int(sys.argv[3]))
    print(((x) * (int(sys.argv[1])-20),y))
        
    red = (red - 20) % 250
    blue = (blue - 20) % 250
    green = (blue + 20) % 255

    # display()
    picture.draw_on_matrix()
    time.sleep((int(sys.argv[2])))


