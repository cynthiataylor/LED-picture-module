# Overview

This is the repository that contains some of the code that supports LED matrices. We used the RGB matrix open-source library but found it hard for beginners in Python because it involves more advanced topics. We already had a Python module to draw patterns, lines, and shapes and edit images. What we needed to change was to display the output to the LED matrices instead of the computer screen.

This repository has folders with different files that you can use to test your LED matrices configuration with a Raspberry Pi4 and the monitor. 

You need to practice and then go to Beta, which has files ready to be run on LED matrices.

## How to use the library we implemented to support LED matrices

There is a Python library we used called Picture. This library has many functions for drawing lines shapes, reading images, editing, and making patterns. 

What you need is to create the canvas for your drawing :
	- import picture

Create a canvas by providing width and height :

	- picture.new_picture(width,height)
 set the background color of the canvas :
 	- picture.set_fill_color(color)
	- use an RGB picture.set_fill_color(red,green,blue)
  
 you need to make the whole canvas change the color( you can draw a rectangle that starts from x = 0 and y = 0 but has a height and width equal to the canvas's dimensions.

To draw a rectangle:

	#- picture.draw_rectangle(x,y,width,height)
To draw a rectangle with a certain color

	#- picture.draw_filled_rectangle(x,y,width,height)

 To display the output on the LED matrix:
 	#- picture.draw_on_matrix()
### How to access the full documentation of the functions with examples.

The full documentation of all modules with all functions you can call to draw can be found here:
	- https://oberlincs.github.io/picture/picture.html

 * But the only difference is that instead of using picture.run() or picture.display(), we use picture.draw_on_matrix(), which shows the output on the LED matrix.
 
 
 


