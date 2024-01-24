import sys

def position(positions = []):

    y = 0
    
    for i in range(int(sys.argv[1])*2):
        positions.append([i,y])
        if i % 4:
            y = 1

    return positions

print(position())

