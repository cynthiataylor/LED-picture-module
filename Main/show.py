from time import sleep
import picture
import random
picture.new_picture(64,64)
picture.set_fill_color("blue")
picture.draw_filled_rectangle(-1,-1,65,65)
picture.set_outline_color("blue")
change = 0
picture.set_position(40,30)


#while True:
angle = 90
angles = [90,180,270,0]
speed = 3
begin = 1
picture.rotate(angle)
j = 0
positions = ''
pos = []
limit = 0
picture.set_pen_width(1)

grow = 64
for i in range(1000000):
	limit += 1
	pos.append(picture.get_position())
	
	change += 1
	picture.set_outline_color('white')
	picture.draw_forward(speed)
	

	
	sleep(0.004)
	picture.draw_on_matrix()
	if len(pos) >0:
		picture.set_fill_color("red")
		picture.set_outline_color("white")
		picture.draw_filled_rectangle(pos[i][0],pos[i][1],5,5)


		
	if (picture.get_position()[0] + 3,picture.get_position()[1] + 3) in pos:
		print("duplicate: ",picture.get_position())
		picture.rotate(random.choice(angles))
		picture.draw_forward(speed)
	if i > 0 and i % 3 == 0:
		picture.rotate(90)
	if len(pos) > 0:
		if pos[-1][0] <= 0 or pos[-1][0] >= 64 or pos[-1][1]  <= 0 or pos[-1][1] + 5 <= 0: 
			print(pos[i])
			picture.set_position(30,30)
			if angle == 90:
				angle = 180
			if angle == 180:
				angle = 0
			if angle == 0:
				angle = 90
			if angle == 90:
				angle = 270
			if angle == 270:
				angle = 0

	





