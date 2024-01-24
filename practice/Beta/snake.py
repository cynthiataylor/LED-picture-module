import picture
import random
import time
import sys

picture.new_picture(int(sys.argv[1]),int(sys.argv[1]))
picture.set_fill_color('white')
picture.draw_filled_rectangle(0,0,int(sys.argv[1]),int(sys.argv[1]))



red = 255
green = 200
blue = 45
x = 1
for i in range(64):
	for j in range(64):
		picture.set_fill_color(red,green,blue)
		picture.draw_forward(j)
		x += 1
		picture.draw_on_matrix()

	red = (red - 20) % 250
	blue = (blue - 20) % 250
	green = (blue + 20) % 255
