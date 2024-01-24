import picture
import random
import time

picture.new_picture(640,64)

# Set initial position 


picture.set_fill_color("black")
picture.set_outline_color("black")
picture.draw_filled_rectangle(0,0,64,64)


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
while True
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
	if pos == 8:
		# print(pos)
		# picture.set_outline_color(red//2,green//3,blue//5)
		pos = 0
		x += 9
		y += 10
		picture.set_position(x,y)
	if x % 10:
		x = random.randint(0,64) if random.randint(0,64) not in taken_pos else random.randint(0,64)
		y = random.randint(0,64) if random.randint(0,64) not in taken_pos else random.randint(0,64)
	if y >= 6:
		y = 0
		x = 2
	# picture.display()
	picture.draw_on_matrix()
	picture.rotate(random.randint(60,65))
	time.sleep(0)
	pos += 1

	red = (red - 2) % 250
	blue = (blue - 20) % 250
	green = (blue + 20) % 255
	
	# print(taken_pos)