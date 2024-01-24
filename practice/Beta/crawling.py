import sys
import picture
import time

picture.new_picture(int(sys.argv[1]),int(sys.argv[1]))
picture.set_fill_color("black")
picture.draw_filled_rectangle(0,0,int(sys.argv[1]),int(sys.argv[1]))

red = 255
green = 200
blue = 45
sec = 1

while True:
    for i in range(200):
        picture.set_fill_color(red,green,blue)
        picture.set_outline_color(red,green,blue)
        picture.set_pen_width(20)
        #picture.set_pen_x(34)
        #picture.set_pen_y(34)
        picture.set_position(int(sys.argv[1])//4,int(sys.argv[1])//4)
        picture.draw_forward(20)
        picture.draw_on_matrix()
        time.sleep(sec)
        picture.set_fill_color("black")
        picture.set_outline_color("black")
        picture.draw_filled_rectangle(0,0,int(sys.argv[1]),int(sys.argv[1]))
        picture.rotate(10)

        # if i == 100:
        #     picture.draw_filled_square(int(sys.argv[1])//2,int(sys.argv[1])//2, 10)
        # if i == 199:
        #     picture.set_fill_color("black")
        #     picture.draw_filled_rectangle(0,0,int(sys.argv[1]),int(sys.argv[1]))
        #     picture.rotate(150)

            
        red = (red - 20) % 250
        blue = (blue - 20) % 250
        green = (blue + 20) % 255
