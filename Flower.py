# sketchy.py

import picture

picture.new_picture(2000,2000)#64-64
picture.set_outline_color(245, 245, 245)
picture.set_fill_color(245, 245, 245)
picture.draw_filled_square(0,0,1500)#64

#Flower drawing
picture.set_fill_color(247, 109, 167)
picture.set_outline_color(250, 62, 141)
picture.set_pen_width(5)
picture.draw_filled_circle(750, 450,300)

#small yellow circle
picture.set_fill_color(250, 214, 97)
picture.draw_filled_circle(750, 450,150)

#green line moving down
picture.set_position(750,750)
picture.set_outline_color(140, 207, 74)
picture.set_pen_width(15)
picture.rotate(90)
picture.draw_forward(750)

# #small line on the right
# picture.set_direction(0)
# picture.set_position(757,1200)
# picture.set_outline_color(140, 207, 74)
# picture.set_pen_width(10)
# picture.draw_forward(90)

# #Small sphere on the right
# picture.set_direction(90)
# picture.set_fill_color(191, 247, 136)
# picture.set_outline_color(140, 207, 74)
# picture.draw_filled_oval(907, 1200, 80, 40)

# #small line on the left
# picture.set_direction(0)
# picture.set_position(757,1000)
# picture.set_outline_color(140, 207, 74)
# picture.set_pen_width(10)
# picture.rotate(180)
# picture.draw_forward(90)


# #Small sphere on the Left
# picture.set_direction(90)
# picture.set_fill_color(191, 247, 136)
# picture.set_outline_color(140, 207, 74)
# picture.draw_filled_oval(590, 1000, 80, 40)


#save
<<<<<<< HEAD
canvas = 64
picture.new_picture(canvas, canvas)

picture.draw_text(10, 2, "EXIT", font_size=1)



beep = True
while beep:
    picture.set_fill_color("red")
    for i in range(30):
        picture.draw_filled_circle(32, 40, 27)

#change the respo
picture.draw_on_matrix()
=======
picture.save_picture("flower.png")
>>>>>>> 1790461 (new changes)
