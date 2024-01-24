# LED-picture-module #

## How to solder to support the 64 pixel board ##

https://learn.adafruit.com/adafruit-rgb-matrix-plus-real-time-clock-hat-for-raspberry-pi/assembly

(Very bottom of page)

## magnetic feet ##

https://www.adafruit.com/product/4631

## Fixing flickering ##

https://learn.adafruit.com/adafruit-rgb-matrix-plus-real-time-clock-hat-for-raspberry-pi/driving-matrices

"The “quality” option comes at a cost. First, you need to solder a jumper wire between GPIO4 and GPIO18 on the Bonnet or Hat board. Also, the normal sound output of the Raspberry Pi must be disabled. You can still use a USB sound adapter if needed, but audio over HDMI or from the 1/8" jack will not be present.

The “convenience” setting requires no changes and sound still works. For many casual projects this might look good enough. There’s an occasional bit of flicker from the matrix, that’s all.

If you’re not sure, or if you just want to get started experimenting with your new gadget, select “convenience” for now. You can make the change and reinstall the software later if needed."

## First steps for converting the picture module: ##

The picture module is based on the PIL library, which the rpi-rgb-led matrix class has support for!

-https://github.com/hzeller/rpi-rgb-led-matrix/blob/master/bindings/python/samples/image-draw.py

To convert the picture library, let's try this:
-Add import statement at the top:

from rgbmatrix import RGBMatrix, RGBMatrixOptions

-In the new_picture function, add

-----
 Configuration for the matrix
options = RGBMatrixOptions()
options.rows = 32 //change to 64
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'adafruit-hat'

matrix = RGBMatrix(options = options) // global class variable
---

We will need to make matrix a global variable

-Add a "draw_on_matrix" function with this code:
matrix.SetImage(IMAGE, 0, 0)

  
