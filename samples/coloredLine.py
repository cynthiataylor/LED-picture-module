import picture
import random
import time

picture.new_picture(128,128)

# Set initial position 

picture.set_fill_color("black")
picture.set_outline_color("black")
picture.draw_filled_rectangle(0,0,128,128)

red = 205
green = 20
blue = 10
size = 2

x = 3
y = 3
picture.set_position(x,y)
runtime = 1
pos = 0
i = 0

taken_pos = []
runtime = 0
while runtime < 300:
	runtime += 1
	taken_pos.append(x)
	taken_pos.append(y)
	picture.set_pen_width(size)
	picture.set_fill_color(red,green,blue)
	picture.set_outline_color(red,green,blue)
	picture.draw_forward(i)
	i += 1
	if i == 4:
		i = 0
	if pos == 60:
		pos = 0
		x += 30
		y += 10
		picture.set_position(x,y)

	# picture.display()
	picture.draw_on_matrix()
	picture.rotate(90)
	time.sleep(0.005)
	pos += 1

	red = (red - 2) % 250
	blue = (blue - 20) % 250
	green = (blue + 20) % 255
	
	# print(taken_pos)