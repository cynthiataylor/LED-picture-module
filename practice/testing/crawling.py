import sys
import picture

picture.new_picture(int(sys.argv[2]),int(sys.argv[2]))
picture.set_fill_color("black")
picture.draw_filled_rectangle(0,0,int(sys.argv[2]),int(sys.argv[2]))

picture.set_fill_color('red')
def snake(positions):
    pos = positions
   


    for i in range(len(positions[-2:])):
        positions[-2:][i][1] += 1
        print(pos)
        while True:
            for i in range(0,len(pos)-1):
                picture.draw_filled_square(pos[i][0] * 50,pos[i][1] * 50,50)
                
                pos = positions[-2:]
                pos.append([(pos[-1][0] + 1),(pos[-1][1])])
                picture.display()
        
    # return pos


argm = int(sys.argv[1])
positions = []
for i in range(argm):
    positions.append([i,0])

snake(positions)
