# sketchy.py
# This program uses the picture module to draw art in Python! Feel free to create something interesting to you. You can find an example in house.py
#
# Would you like your artwork to be included in the CSCI gallery?
# [x] Yes, I give permission to use my name and artwork in the CSCI 150 gallery.


import picture
import random

red = 30
green = 250
blue = 200
picture.new_picture(1000, 1000)
picture.set_fill_color("black")
picture.draw_filled_square(0,0,1000)

for k in range(100):
    # picture.set_pen_width(8)
    picture.set_position(400,500)
    picture.set_fill_color("white")
    picture.draw_forward(2 * k)
    picture.rotate(60)
    picture.display()

# throwing dots on the wall
for i in range(1,100):
    picture.set_fill_color(red,green,blue)
    x = random.randrange(1000)
    y = random.randrange(1000)
    
    picture.draw_filled_square(x,y,10)

    green = (green + 20) % 255
    blue = (blue - 20) % 255
    picture.display()
    
#draw the square on the wall
for i in range(100):
    for i in range(500):
        picture.draw_square(10,10,2+i*2)
        picture.rotate(10*i)
        picture.display()

#draw the lines from the center and shape line beam
for i in range(100000):
    picture.set_outline_color(red,green,blue)
    picture.set_pen_width(3)
    picture.set_position(500,500)
    
    picture.draw_forward(4*i)
    picture.rotate(60 + i)

    green = (green + 20) % 255
    blue = (blue - 20) % 255
    red = (red - 20) % 255
    picture.display()


# draw a circle and rotate from the center the canvas set
for k in range(200):
    picture.set_position(500,500)
    picture.set_outline_color(red,green,blue)
    picture.set_fill_color("white")

    for l in range(k):
        picture.draw_forward(70 + k)
        picture.rotate(60)
        picture.display()
    
    #drawing the other circle rotated different ratations and forward size

    picture.set_position(500,500)
    picture.set_outline_color("white")
    picture.set_fill_color("red")
    for l in range(k):
        picture.draw_forward(70 + k + 2)
        picture.rotate(60)
        picture.display()

    red = 0
    picture.set_position(500,500)
    picture.set_outline_color("springgreen")
    picture.set_fill_color(red,green,blue)
    for l in range(k):
        picture.draw_forward(70 + i)
        picture.rotate(60)
        picture.display()

    
    green = (green + 20) % 255
    blue = (blue - 20) % 255

# picture.save_picture("sketchy.png")
    # picture.display()