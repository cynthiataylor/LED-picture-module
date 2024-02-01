This is the repository that contains some of the code that supports LED matrices. We used the open-source library called RGB matrix but we found it hard to use for beginner in pyhton because it involves more advanced topics. We already had a python module that can draw draw patterns, lines, shapes , and also edit images. What we needed to change what to display the output to the LED matrices instead of the computer screen.

In this repository, there are folders and those have different files that you can use to test your LED matrices configuration with a raspberry pi4 and the monitor. 

You need to to practice, then go to Beta which has files ready to be run on LED matrices.


There is a python library we used which is called picture. In this library, there are many functions for drawing lines, drawing shapes, reading images and also editing them, makin patterns. 

What you need, is to create canvas for your drawing :
	- import picture

Create a canvas by providing width and the height :

	- picture.new_picture(width,height)
 set the background color of the canvas :
 	- picture.set_fill_color("red") or use RGB picture.set_fill_color(255,0,0)
  
 you need to make the whole canvas changes the color( you can draw a rectangle that starts from x = 0 and y = 0 but have the height and width that are equal to the dimensions of the canvas.

To draw a rectangle :

	- picture.draw_rectangle(x,y,width,height)
To draw a rectangle with the a certain color

	- picture.draw_filled_rectangle(x,y,width,height)

 To display the output on the LED matrix

 picture.display()
 
 


