import picture
import time

# Create a turtle object
picture.new_picture(800,800)

# Set initial position and angle
x, y = 0, 0
angle = 40

# Set up the turtle's appearance
time.sleep(0)  # Set the drawing speed (0 is the fastest)
# picture.set_pen_width(2) # Set the width of the pen
# picture.set_outline_color("blue")
# picture.set_fill_color("white")  # Set the shape of the turtle

# Draw the spiral
picture.set_position(350,350)
for i in range(2000):

    picture.draw_forward(13 + i)
    picture.rotate(140)
    picture.draw_forward(-10)
    
    angle += 1
    picture.display()