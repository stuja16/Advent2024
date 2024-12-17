# Must input a correct answer for part 1 before part 2 can be viewed
# https://adventofcode.com/2024/day/10#part2

def solve(fileName):
    score = 0

    # Create territory grid
    lines = open(fileName,"r").readlines()
    h, w = len(lines), len(lines[0])-1  # -1 to account for newline characters
    grid = {(y,x):lines[y][x] for y in range(h) for x in range(w)}

    # Find trailheads
    for y,x in grid:
        if grid[y,x] == "0":
            score += findNextNumber(y,x,0,grid,h,w)

    return score

def findNextNumber(y,x,curNum,grid,h,w):
    if curNum == 9:
        return 1
    
    score = 0
    nextNum = curNum+1
    
    if y>0 and grid[y-1,x] == str(nextNum): # Check up
        score += findNextNumber(y-1,x,nextNum,grid,h,w)
    if x<w-1 and grid[y,x+1] == str(nextNum): # Check right
        score += findNextNumber(y,x+1,nextNum,grid,h,w)
    if y<h-1 and grid[y+1,x] == str(nextNum): # Check down
        score += findNextNumber(y+1,x,nextNum,grid,h,w)
    if x>0 and grid[y,x-1] == str(nextNum): # Check left
        score += findNextNumber(y,x-1,nextNum,grid,h,w)

    return score
    
print(solve("Day10/UnitTest.txt"))
print(solve("Day10/input.txt"))