
def position(positions = []):

    for x in range(64):
        for y in range(64):
            positions.append([x,y])
    return positions

print(position())
