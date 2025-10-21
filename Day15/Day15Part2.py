# Must input a correct answer for part 1 before part 2 can be viewed
# https://adventofcode.com/2024/day/15#part2

from collections import deque

def solve(fileName):
    # Format input data
    grid, instructions = open(fileName,"r").read().strip().split("\n\n")
    instructions = list(instructions.replace('\n', ''))

    # Upscale grid
    robot = findRobot([list(x) for x in grid.split("\n")])
    grid = grid.replace(".","..").replace("#","##").replace("O","[]").replace("@","..").split("\n")
    grid = [list(x) for x in grid]

    # Run simulation
    for i in instructions:
        match i:
            case "<":
                grid, robot = move(grid, *robot, -1, 0)
            case ">":
                grid, robot = move(grid, *robot, 1, 0)
            case "v":
                grid, robot = move(grid, *robot, 0, 1)
            case "^":
                grid, robot = move(grid, *robot, 0, -1)

    # Calculate sum
    sum = 0
    for r,row in enumerate(grid):
        for c,val in enumerate(row):
            if val == "[":
                sum += r*100+c
    return sum


# Find the robot in the grid
# Used at the start of the simulation to get an initial position
def findRobot(grid):
    for r,row in enumerate(grid):
        for c,val in enumerate(row):
            if val == "@":
                return (r,c*2)  # Double horizontal position for resizing
    return -1

def move(grid,y:int,x:int,dx:int,dy:int):
    newRobotPos = (y+dy,x+dx)

    # Check if robot can legally move
    hitWall = False
    rockQ = deque()     # Queue of next spaces to check for collisions
    rockQ.append(newRobotPos)
    oldRocks = set()    # Set of rocks to delete if move is legal
    newRocks = set()    # Set of rocks to add after movement if legal
    while rockQ and not hitWall:
        ny,nx = rockQ.popleft()
        match grid[ny][nx]:
            case "#":
                hitWall = True
                break
            case "[":
                if (ny+dy,nx+dx) not in oldRocks:
                    rockQ.append((ny+dy,nx+dx))
                if (ny+dy,nx+dx+1) not in oldRocks:
                    rockQ.append((ny+dy,nx+dx+1))
                oldRocks.add((ny,nx))
                oldRocks.add((ny,nx+1))
                newRocks.add((ny+dy,nx+dx,"["))
                newRocks.add((ny+dy,nx+dx+1,"]"))
            case "]":
                if (ny+dy,nx+dx) not in oldRocks:
                    rockQ.append((ny+dy,nx+dx))
                if (ny+dy,nx+dx-1) not in oldRocks:
                    rockQ.append((ny+dy,nx+dx-1))
                oldRocks.add((ny,nx))
                oldRocks.add((ny,nx-1))
                newRocks.add((ny+dy,nx+dx,"]"))
                newRocks.add((ny+dy,nx+dx-1,"["))

    # If check fails, don't move anything
    if hitWall:
        return grid, (y,x)

    for y,x in oldRocks:
        grid[y][x] = "."
    for y,x,val in newRocks:
        grid[y][x] = val

    return grid, newRobotPos

print(solve("Day15/UnitTest2.txt"))
print(solve("Day15/input.txt"))