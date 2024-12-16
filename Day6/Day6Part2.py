# Must input a correct answer for part 1 before part 2 can be viewed
# https://adventofcode.com/2024/day/6#part2

# This code is very unoptimized, so it takes ~5 minutes to run on the full input data
# The only optimization made is the choice to only try placing obstacles on the path where the guard goes
# It might be better to try placing an obstacle immediately as the guard is walking around instead of making
# those separate processes? Then I wouldn't have to repeatedly pathfind through the same irrelevant parts of the
# map.
# Also parallel processing, but I don't remember enough of how to do that in python atm

import copy

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
    startingCoords = coords
    positions = set() # Using a "set" of positions ensures there are no repeats

    # Track each movement of the guard without any added obstacles to get a list of all visited tiles
    # It's only worth trying to add obstacles where the guard might run into them
    while 0<=coords[0]+delta[0]<h and 0<=coords[1]+delta[1]<w:
        nextTile = [x + y for x, y in zip(coords, delta)]
        if grid[nextTile[0],nextTile[1]]=="#": # If hitting obstacle, turn!
            delta = turn(delta)
            continue 
        coords = nextTile
        positions.add(tuple(coords))

    # Remove starting coords from the set IF they were added b/c can't place an obstacle on top of the guard
    positions.discard(tuple(startingCoords))

    possibleObstructions = 0    # Final answer
    for y,x in positions:
        # Add new obstacle
        newGrid = copy.deepcopy(grid)
        newGrid[y,x] = "#"

        # Check for loops
        possibleObstructions += createsLoop(h,w,newGrid,[-1,0],startingCoords[:])        

    return possibleObstructions

def turn(delta):
    if delta==[-1,0]:
        return [0,1]
    elif delta==[0,1]:
        return [1,0]
    elif delta==[1,0]:
        return[0,-1]
    return [-1,0]

# Returns boolean: True if the given grid traps the guard in a loop
def createsLoop(h,w,grid,delta,coords):
    # Keep track of position and direction every time you hit an obstacle
    # If we get the same values twice, we've created a loop
    hittingObstacles = set()

    # Navigate the guard through the lab
    while 0<=coords[0]+delta[0]<h and 0<=coords[1]+delta[1]<w:
        nextTile = [x + y for x, y in zip(coords, delta)]

        if grid[nextTile[0],nextTile[1]]=="#": # If hitting obstacle, turn!
            # Loop checking
            state = (coords[0],coords[1],delta[0],delta[1])
            if state in hittingObstacles:
                return True
            hittingObstacles.add(state) # Log state if loop not created yet

            delta = turn(delta)
            continue    # Don't move forward

        coords = nextTile
    
    return False
    
print(solve("Day6/UnitTest.txt"))
print(solve("Day6/input.txt"))