# name = '\n'.join([''.join([('computerscience'[(x-y) % len('computerscience')] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else' ') for x in range(-30, 30)]) for y in range(30, -30, -1)])

# print(name)
import time
import picture
picture.new_picture(500,500)
picture.set_fill_color('black')
picture.draw_filled_rectangle(0,0,500,500)



def realtime():
    for i in range(2000):
        picture.set_fill_color('black')
        picture.draw_filled_rectangle(0,0,500,500)

        picture.set_outline_color("white")

        times = time.ctime()
        picture.draw_text(100,100,times,30)
        picture.display()
def clock():
    picture.draw_filled_circle(200,200,200)
    picture.set_fill_color("black")
    picture.set_outline_color('black')

    picture.set_pen_width(3)
    picture.set_pen_x(200)
    picture.set_pen_y(200)
    picture.set_outline_color('white')

    picture.draw_forward(200)
    picture.rotate(10)
    picture.display()
    time.sleep(1)
    picture.set_fill_color('black')
    picture.draw_filled_rectangle(0,0,500,500)

# for i in range(10000):
#     clock()


for i in range(12):
