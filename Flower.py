import picture
import time

canvas = 64
picture.new_picture(canvas, canvas)



picture.draw_text(10, 2, "EXIT", font_size=1)

beep = True
while beep:
    for i in range(30):
        picture.draw_filled_circle((32, 40, 27), fill="red", outline = "red")
        time.sleep(0.1)


picture.draw_on_matrix()
