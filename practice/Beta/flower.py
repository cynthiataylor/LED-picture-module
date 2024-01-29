import picture
import time
import sys

picture.new_picture(128,128)
picture.set_fill_color("black")
picture.draw_filled_rectangle(0,0,128,128)

red = 30
green = 250
blue = 200

pause = 0

for i in range(0,60):
    for k in range(50):
        picture.set_outline_color(red,green,blue)
        picture.draw_circle(1*(k*3),i*4,4)
        picture.draw_on_matrix()
        pause +=1
        if pause >= 1500:
            sys.exit()
    
    green = (green + 20) % 255
    red = (red - 20) % 250
    
