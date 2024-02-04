import picture

picture.new_picture(128,128)
picture.set_fill_color("green")

picture.draw_filled_square(64,64,30)
while True:
    picture.draw_on_matrix()


