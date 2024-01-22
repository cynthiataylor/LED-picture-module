import picture
from time import sleep
#save
canvas = 64

picture.new_picture(canvas, canvas)

picture.set_fill_color("black")
picture.draw_filled_rectangle(-1,-1,65,65)

color = "red"

position = 0
text = "Winter"

while True:
	color = 'black' if color == "red" else 'red'
	picture.set_fill_color(color)
	picture.set_outline_color(color)
	picture.draw_filled_circle(32,35,27)
	print(color)
	picture.draw_on_matrix()
	sleep(1)


    



