import sys
import picture
import time

picture.new_picture(128,128)
picture.set_fill_color("black")
picture.draw_filled_rectangle(0,0,128,128)

red = 255
green = 200
blue = 45

runtime = 10
# while runtime > 0: 
    
for i in range(35):
    print(i)
    runtime -=1
    picture.set_fill_color(red,green,blue)
    picture.set_outline_color(red,green,blue)
    picture.set_pen_width(40)
    # picture.set_pen_x(300)
    # picture.set_pen_y(300)
    picture.set_position(128//2,128//2)
    picture.draw_forward(i * 2)
    picture.draw_on_matrix()
    time.sleep(0.5)
    picture.draw_forward(46)
    picture.rotate(10)

    picture.set_fill_color("black")
    picture.set_outline_color("black")
    picture.draw_filled_rectangle(0,0,128,128)
    

        
    red = (red - 20) % 250
    blue = (blue - 20) % 250
    green = (blue + 20) % 255