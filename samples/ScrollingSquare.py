import picture as picture
import random
import time
import sys

picture.new_picture(128,128)
picture.set_fill_color("black")
picture.draw_filled_rectangle(0,0,128,128)

red = 255
green = 200
blue = 23

y = 0
x = 0

down = 120
up = 120

positions = []
counter = 0

runtime = 100
while True:
    for t in range(4):
        runtime -=1
        x+= 1

        picture.set_fill_color(red,green,blue)
        
        picture.draw_filled_square(x,y,10)
        picture.draw_filled_square(y,x,10)
        picture.draw_filled_square(up,down,10)
        picture.draw_filled_square(down,up,10)
        if counter % 50 == 0:
            picture.draw_filled_square(random.randint(3,120),random.randint(3,120),10)
        
        
        if x >=128:
            x = 0
            y += 4
        if y >= 128:
            y = 0
            x = 0
            
        if up <=4:
            up = 120
            down -= 2
        if down <=4:
            down = 120
            up = 120
        counter += 1
        #down -= 1
        up -=2
  
        picture.draw_on_matrix()


        blue = (blue - 4) % 255 
        #red = (red - y) % 255
        green = (green //(x + 1))%255
        
