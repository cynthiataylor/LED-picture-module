import picture
import time
#save
canvas = 64

picture.new_picture(canvas, canvas)

#picture.draw_text(10, 2, "EXIT", font_size = 12)
color = 'red'
picture.set_fill_color("black")
picture.draw_filled_square(0, 0, canvas)
while True:
    
    color = 'red' if color == 'blue' else 'blue'
    
    #picture.set_outline_color(color)
    print(color)
    picture.set_fill_color(color)
    picture.draw_circle(32, 32, 27)
    
    picture.draw_on_matrix()

    time.sleep(1)
    



