from picture import *
import picture
import time
import random
import sys

class Grid:

    def __init__(self,cols,rows,size):
        self.cols = cols
        self.rows = rows
        self.size = size
        self.positions = []
        self.gridPos = []

        random.shuffle(self.positions)
    
    def setup(self):
        new_picture(self.rows,self.cols)
        

    def background(self):
        grid.setup()
        
        set_fill_color(33, 4, 64)
        set_outline_color("white")
        draw_filled_rectangle(0,0,self.rows,self.cols)
    
    def drawGrid(self):
        grid.background()


        for row in range(self.rows//self.size):
            for cols in range(self.cols//self.size):
                # set_outline_color("white")
                draw_square(self.rows// 16 + (row * self.size),self.cols//16 + (cols * self.size),self.size)
                self.positions.append([self.rows//16 + (row * self.size),self.cols//16 + (cols * self.size)])
        return grid.positions

    def matrix(self):
        for i in range(self.rows//self.size):
            for j in range(self.cols//self.size):
                self.gridPos.append(random.randrange(2))
        return grid.gridPos

    def dead(self,position):
        set_fill_color("red")
        set_outline_color("red")
        draw_filled_square(random.choice(position)[0],random.choice(position)[1],self.size)

    def alive(self,position):
        set_fill_color("white")
        set_outline_color("white")
        draw_filled_square(random.choice(position)[0],random.choice(position)[1],self.size)

    def output(self,matrix,position):
        grid.drawGrid()

        for i in range(len(matrix)):
            if matrix[i] == 0:
                grid.dead(position)
   
            elif matrix[i] == 5:
                grid.alive(position)
        return matrix

             
grid = Grid(128,128,int(sys.argv[1]))
grid2 = Grid(128,128,int(sys.argv[1])) 

matrix = grid.matrix()
position = grid.positions
color = 'white'

for i in range(50):
    
    # if i > 0 and i % 5 == 0:
    grid.output(matrix,position)
    picture.draw_on_matrix()
    time.sleep(1)

