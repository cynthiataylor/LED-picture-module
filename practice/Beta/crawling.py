import sys
import picture
import time

picture.new_picture(int(sys.argv[1]),int(sys.argv[1]))
picture.set_fill_color("black")
picture.draw_filled_rectangle(0,0,int(sys.argv[1]),int(sys.argv[1]))

red = 255
green = 200
blue = 45

sec = 0.005
move = 100
top = 100
bottom = 0
right = 5
left = 5
back = 64
x = 5
y = 100
while True:
    for i in range(2000):
        picture.set_fill_color(red,green,blue)
        picture.set_outline_color(red,green,blue)
        picture.set_pen_width(20)
        #picture.set_pen_x(34)
        #picture.set_pen_y(34)
        picture.set_position(int(sys.argv[1])//2,int(sys.argv[1])-30)
        picture.draw_forward(20)
        picture.draw_on_matrix()
        time.sleep(sec)
        picture.set_fill_color("black")
        picture.set_outline_color("black")
        picture.draw_filled_rectangle(0,0,int(sys.argv[1]),int(sys.argv[1]))
        picture.rotate(50)

        picture.set_outline_color(red,green,blue)
        picture.draw_text(move,25,"Welcome to computer science department",30)
        move -= 1
        if move == -100:
                move = 100
        picture.draw_filled_circle(x,y,4)
        
        
        if y <= 10:
                y = right
                x = left
                left +=1
        if left >=64:
                y = bottom
                
                x = 64
                bottom +=1
        y -=1
        
        if bottom <= 64:
                print(bottom)
                
            
        red = (red - 20) % 250
        blue = (blue - 20) % 250
        green = (blue + 20) % 255
