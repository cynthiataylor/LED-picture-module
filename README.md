# LED-picture-module #

## How to solder to support the 64 pixel board ##

https://learn.adafruit.com/adafruit-rgb-matrix-plus-real-time-clock-hat-for-raspberry-pi/assembly

(Very bottom of page)

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
options.rows = 32
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'adafruit-hat'

matrix = RGBMatrix(options = options)

---

We will need to make matrix a global variable

-Add a "draw_on_matrix" function with this code:
matrix.SetImage(IMAGE, 0, 0)

  
