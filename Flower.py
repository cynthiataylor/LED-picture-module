import picture
import time

canvas = 64
picture.new_picture(canvas, canvas)

picture.draw_text(10, 2, "EXIT", font_size=1)

picture.draw_text((10, 2), "EXIT", 1)

beep = True
while beep:
    picture.set_fill_color("red")
    for i in range(30):
        picture.draw_filled_circle(32, 40, 27)
        time.sleep(0.1)

#cvf
picture.draw_on_matrix()
