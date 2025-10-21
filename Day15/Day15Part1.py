# https://adventofcode.com/2024/day/15

def solve(fileName):
    # Format input data
    grid, instructions = open(fileName,"r").read().strip().split("\n\n")
    grid = [list(x) for x in grid.split("\n")]
    instructions = list(instructions.replace('\n', ''))

    # Run simulation
    robot = findRobot(grid)
    grid[robot[0]][robot[1]] = "."  # Remove robot to prevent later collisions
    for i in instructions:
        match i:
            case "<":
                grid, robot, _ = move(grid, robot, -1, 0, False)
            case ">":
                grid, robot, _ = move(grid, robot, 1, 0, False)
            case "v":
                grid, robot, _ = move(grid, robot, 0, 1, False)
            case "^":
                grid, robot, _ = move(grid, robot, 0, -1, False)

    # Calculate sum
    sum = 0
    for r,row in enumerate(grid):
        for c,val in enumerate(row):
            if val == "O":
                sum += r*100+c
    return sum


# Find the robot in the grid
# Used at the start of the simulation to get an initial position
def findRobot(grid):
    for r,row in enumerate(grid):
        for c,val in enumerate(row):
            if val == "@":
                return (r,c)
    return -1

# Attempt to move the block in the specified direction
# Can only move orthogonally 1-square
def move(grid,pos:tuple[int,int],dx:int,dy:int,boxFound:bool):
    # If ., set as the previously found object (robot or box)
        # Set current space as box "if needed"
        # Move back to last iteration
        # Only the first iteration should return coordinates, the others only need to return the grid
    # If O, move to check the next loc linearly
    # If #, return with no changes
    newPos = (pos[0]+dy,pos[1]+dx)
    match grid[newPos[0]][newPos[1]]:
        case ".":
            if not boxFound:
                return grid,newPos,True
            else:
                grid[newPos[0]][newPos[1]] = "O"
                return grid,newPos,True
        case "O":
            grid,_,success = move(grid,newPos,dx,dy,True)
            if success:     # AKA robot can move in this direction
                if not boxFound:
                    grid[newPos[0]][newPos[1]] = "."    # If robot is entering square previously held by box, clear it
                return grid, newPos, True
            else:           # AKA robot cannot move in this direction, hit wall
                return grid, pos, False
        case "#":
            return grid,pos,False

print(solve("Day15/UnitTest1.txt"))
print(solve("Day15/input.txt"))