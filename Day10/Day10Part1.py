# https://adventofcode.com/2024/day/10

def solve(fileName):
    score = 0

    # Create territory grid
    lines = open(fileName,"r").readlines()
    h, w = len(lines), len(lines[0])-1  # -1 to account for newline characters
    grid = {(y,x):lines[y][x] for y in range(h) for x in range(w)}

    # Find trailheads
    for y,x in grid:
        if grid[y,x] == "0":
            # Set of the coordinates of all 9s reachable from this trailhead
            destsReached = set()
            findNextNumber(y,x,0,grid,h,w,destsReached)
            score += len(destsReached)

    return score

def findNextNumber(y,x,curNum,grid,h,w,dests):
    if curNum == 9:
        dests.add((y,x))
        return
    
    nextNum = curNum+1
    
    if y>0 and grid[y-1,x] == str(nextNum): # Check up
        findNextNumber(y-1,x,nextNum,grid,h,w,dests)
    if x<w-1 and grid[y,x+1] == str(nextNum): # Check right
        findNextNumber(y,x+1,nextNum,grid,h,w,dests)
    if y<h-1 and grid[y+1,x] == str(nextNum): # Check down
        findNextNumber(y+1,x,nextNum,grid,h,w,dests)
    if x>0 and grid[y,x-1] == str(nextNum): # Check left
        findNextNumber(y,x-1,nextNum,grid,h,w,dests)

    return
    
print(solve("Day10/UnitTest.txt"))
print(solve("Day10/input.txt"))