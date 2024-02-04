import picture as picture
import time
import random


picture.new_picture(128,128)

# Set initial position 
x, y = 40, 20




picture.set_fill_color(33, 4, 64)
picture.set_outline_color(33, 4, 64)
picture.draw_filled_rectangle(0,0,128,128)

red = 255
green = 200
blue = 45
i = 0

change = 20
delete = 0
angle = 100

picture.set_position(x,y)
		
runtime = 1000
while runtime > 0:
	runtime -=1
	i += 1
	delete += 1
	picture.set_outline_color(red,green,blue)
	picture.draw_forward(i//5)
	picture.rotate(angle)
	angle += 1
	picture.draw_on_matrix()
	#time.sleep(0.0000000001)
	
	if angle == 180:
		angle = random.randint(60,160)
	
	
	if i == change//6:
		picture.set_fill_color("black")
		picture.set_outline_color("black")
		picture.draw_filled_rectangle(0,0, delete,delete)
		#i = 0
		change += 1
	if i == 20:
		i = 0
	if change == 60:
		change = 20
	if delete == 128:
		delete = 0
	
	if picture.get_position()[0] <=0 or picture.get_position()[1] <=0 or picture.get_position()[0] <=64 or picture.get_position()[1] <=64:
		x = random.randint(10,45)
		y = random.randint(10,45)
	
	
	
	picture.set_outline_color("orange")
	picture.draw_forward(10 % change)
	picture.set_outline_color("white")
	picture.draw_forward(1 % change)
	time.sleep(0)
	red = (red - 20) % 250
	blue = (blue - 20) % 250
	green = (blue + 20) % 255
	
