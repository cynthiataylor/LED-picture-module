import picture
from time import sleep
#save
canvas = 128

picture.new_picture(canvas, canvas)




picture.set_fill_color("black")
picture.draw_filled_rectangle(-1,-1,129,129)

color = "red"


while True:
	color = 'black' if color == "red" else 'red'
	
	picture.set_fill_color("red")
	picture.set_outline_color("red")
	picture.draw_text(34,0, "EXIT", 28)
	
	picture.set_fill_color(color)
	picture.set_outline_color(color)
	picture.draw_filled_circle(64,76,46)
	#print(color)
	picture.draw_on_matrix()
	sleep(1)


    



