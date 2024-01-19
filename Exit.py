import picture
import time
#save
canvas = 64
picture.new_picture(canvas, canvas)

picture.draw_text(10, 2, "EXIT", font_size = 6)



beep = True
while beep:
    picture.set_fill_color("red")
    picture.draw_filled_circle(32, 40, 27)
    picture.display()
    time.sleep(2)

    picture.set_fill_color("black")
    picture.draw_filled_circle(32, 40, 27)
    picture.display()
    time.sleep(2)



