# https://adventofcode.com/2024/day/6

def solve(fileName):
    lines = open(fileName,"r").readlines()
    h, w = len(lines), len(lines[0])-1  # -1 to account for newline characters
    grid = {(y,x):lines[y][x] for y in range(h) for x in range(w)}
    delta = [-1,0]

    # Find guard's starting position
    for y,x in grid:
        if grid[y,x]=="^":
            coords = [y,x]
            break
    positions = {tuple(coords)} # Set of positions ensures there are no repeats

    # Track each movement of the guard
    while 0<=coords[0]+delta[0]<h and 0<=coords[1]+delta[1]<w:
        nextTile = [x + y for x, y in zip(coords, delta)]
        if grid[nextTile[0],nextTile[1]]=="#": # If hitting obstacle, turn!
            delta = turn(delta)
            continue 
        coords = nextTile
        positions.add(tuple(coords))

    return len(positions)

def turn(delta):
    if delta==[-1,0]:
        return [0,1]
    elif delta==[0,1]:
        return [1,0]
    elif delta==[1,0]:
        return[0,-1]
    return [-1,0]
    
print(solve("Day6/UnitTest.txt"))
print(solve("Day6/input.txt"))