# Must input a correct answer for part 1 before part 2 can be viewed
# https://adventofcode.com/2024/day/20#part2

def solve(fileName,threshhold):
    grid = [list(r) for r in open(fileName,"r").read().strip().split("\n")]

    # Find start and end coords
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'S':
                start = (i,j)
            elif grid[i][j] == 'E':
                end = (i,j)

    path = djikstra(grid,start,end)

    # Check how many shortcuts save time >= threshhold
    cheats = set()  # Prevent repeat w/ diff path but same start/end tiles
    for i in range(len(path)):
        for j in range(i+1,len(path)):
            (y1,x1),dist1 = path[i]
            (y2,x2),dist2 = path[j]

            cheat = (y1,x1,y2,x2)
            cheatDist = abs(y2-y1)+abs(x2-x1)
            if cheatDist <= 20 and dist2-dist1 >= threshhold + cheatDist:
                cheats.add(cheat)

    return len(cheats)

# Find best path w/o cheating
def djikstra(grid,start,end):
    time = 0
    path = []
    path.append((start,time))
    visited = set()
    visited.add(start)
    loc = start

    while not loc == end:
        y,x = loc
        time += 1

        # Move to adjacent cells:
        downPos = (y+1,x)
        upPos = (y-1,x)
        leftPos = (y,x-1)
        rightPos = (y,x+1)
        if downPos not in visited and not grid[downPos[0]][downPos[1]] == '#':
            loc = downPos
            path.append((downPos,time))
            visited.add(downPos)
        elif upPos not in visited and not grid[upPos[0]][upPos[1]] == '#':
            loc = upPos
            path.append((upPos,time))
            visited.add(upPos)
        elif leftPos not in visited and not grid[leftPos[0]][leftPos[1]] == '#':
            loc = leftPos
            path.append((leftPos,time))
            visited.add(leftPos)
        elif rightPos not in visited and not grid[rightPos[0]][rightPos[1]] == '#':
            loc = rightPos
            path.append((rightPos,time))
            visited.add(rightPos)

    return path

print(solve("Day20/UnitTest.txt",70))
print(solve("Day20/input.txt",100))