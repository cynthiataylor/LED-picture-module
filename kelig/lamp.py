import picture
from time import sleep

picture.new_picture(64,64)


picture.set_fill_color("green")
picture.draw_filled_rectangle(0,0,64,64)

color = "red"

for i in range(10):
	color = 'blue' if color == "red" else 'red'
	picture.set_fill_color(color)
	picture.set_outline_color(color)
	picture.draw_filled_circle(10,10,10)
	print(color)
	picture.draw_on_matrix()
	sleep(3)
