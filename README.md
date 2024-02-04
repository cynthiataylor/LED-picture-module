# Overview

This is the repository that contains some of the code that supports LED matrices. We used the RGB matrix open-source library but found it hard for beginners in Python because it involves more advanced topics. We already had a Python module to draw patterns, lines, and shapes and edit images. What we needed to change was to display the output to the LED matrices instead of the computer screen.

This repository has folders with different files that you can use to test your LED matrices configuration with a Raspberry Pi4 and the monitor. 

You need to go to practice and then to Beta, which has files ready to run on LED matrices.

## How to use the library we implemented to support LED matrices
> [!NOTE]
> You need to have knowledge of Python to be able to use this library.

There is a Python library we used called Picture. This library has many functions for drawing lines shapes, reading images, editing, and making patterns. 

What you need is to create the canvas for your drawing :

	import picture

Create a canvas by providing width and height :

	picture.new_picture(width,height)

 Set the background color of the canvas :
 
 	picture.set_fill_color(color)
 
	use an RGB picture.set_fill_color(240,50,200)

 You need to make the whole canvas change the color( you can draw a rectangle that starts from x = 0 and y = 0 but has a height and width equal to the canvas's dimensions.

To draw a rectangle:

	picture.draw_rectangle(0,0,width,height)

To draw a rectangle with a certain color

	picture.draw_filled_rectangle(x,y,width,height)

 To display the output on the LED matrix:

 	picture.draw_on_matrix()
 
### How to access the full documentation of the functions with examples.

The full documentation of all modules with all functions you can call to draw can be found here:

https://oberlincs.github.io/picture/picture.html

 * But the only difference is that instead of using `

		picture.run()
		picture.display()

To display the output on the matrix, you need to use :

	picture.draw_on_matrix()

> [!CAUTION]
> Make use after writing the code; you do picture.draw_on_matrix() to display the drawing on the LED matrix.

> [!TIP]
> THe sample code that draws a red square on the LED matrix

	import picture
	
	def set_canvas(width,height): # a function that set the canvas
		picture.new_picture(width,height) # to set the canvas 
		picture.set_fill_color("black") # to set the background color
		picture.set_outline_color("black") # setting the color of the pen
		picture.draw_filled_rectangle(0,0, width, height) # drawing the rectangle that fits the canvas to be all the same color
	
	def graph_square(width,height):
		set_canvas(width, height) # Draw the canvas by calling the function.
		picture.set_fill_color("red") 
		picture.set_outline_color("red")
		picture.draw_filled_square(width//2,height//2,width//4)
		picture.draw_on_matrix() # to display on the matrix
	
	
	# The width and the height will depend on the size of your LED matrix
	width = 64
	height = 64
	graph_square(width, height) # Call the function that draws the square on the matrix
		
	 

 	
 ### For the programs well prepared for LED matrices in practice/Beta :

 There is a file called file_runner, which is for running each other files in the same directory/ folder.

It works using the library called os and subprocess, which manages running processes. If you don't want it to run some of the
files, there is a list that excludes it; you can add any file you want to exclude from running.


If you haven't used these libraries, they are very easy to learn, and you can use the official Python documentation on os/subprocess here:

- https://docs.python.org/3/library/os.html#file-names-command-line-arguments-and-environment-variables
- cheatsheet of all its methods: https://www.w3schools.com/python/module_os.asp
- More simplified: https://www.tutorialsteacher.com/python/os-module

  



 
 


