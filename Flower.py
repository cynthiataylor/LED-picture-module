import picture
import time
import keyboard

canvas = 64
picture.new_picture(canvas, canvas)

def stop_beep(_): #You need to test this one
    global beep
    beep = False

keyboard.add_hotkey("Ctrl+C", stop_beep)

picture.draw_text((10, 2), "EXIT", 1)
beep = True
while beep:
    for i in range(30):
        picture.draw_filled_circle((32, 40, 27), fill="red", outline = "red")
        time.sleep(0.1)


picture.draw_on_matrix()
