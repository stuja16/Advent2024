# https://adventofcode.com/2024/day/16
# Solved with Djikstra's algorithm

from heapq import heappop, heappush

def solve(fileName):
    grid = [list(x) for x in open(fileName,"r").read().strip().split("\n")]

    startPos = (len(grid)-2,1)
    startDir = (0,1)
    minScore = float('inf')

    # Setup data structures for djikstra
    pq = []             # Min queue of valid ways to continue the path
    heappush(pq,(0,(startPos,startDir)))
    visited = set()     # Track visited coords to prevent loops/repeats
    visited.add(startPos)

    # Run djikstra
    while pq:
        curScore, ((y,x),(dy,dx)) = heappop(pq)

        # Break if end of path
        if grid[y][x] == "E":
            minScore = min(minScore, curScore)
            break

        # Branch out in forward direction:
        nextPos = (y+dy,x+dx)
        if nextPos not in visited and not grid[y+dy][x+dx] == "#":
            heappush(pq,(curScore+1,(nextPos,(dy,dx))))
            visited.add(nextPos)

        # If moving E or W, check N/S
        if dy == 0:
            dy,dx = 1,0
            nextPos = (y+dy,x+dx)
            if nextPos not in visited and not grid[y+dy][x+dx] == "#":
                heappush(pq,(curScore+1001,(nextPos,(dy,dx))))
                visited.add(nextPos)
            dy,dx = -1,0
            nextPos = (y+dy,x+dx)
            if nextPos not in visited and not grid[y+dy][x+dx] == "#":
                heappush(pq,(curScore+1001,(nextPos,(dy,dx))))
                visited.add(nextPos)
        else:   # Check E/W
            dy,dx = 0,1
            nextPos = (y+dy,x+dx)
            if nextPos not in visited and not grid[y+dy][x+dx] == "#":
                heappush(pq,(curScore+1001,(nextPos,(dy,dx))))
                visited.add(nextPos)
            dy,dx = 0,-1
            nextPos = (y+dy,x+dx)
            if nextPos not in visited and not grid[y+dy][x+dx] == "#":
                heappush(pq,(curScore+1001,(nextPos,(dy,dx))))
                visited.add(nextPos)

    return minScore

print(solve("Day16/UnitTest.txt"))
print(solve("Day16/input.txt"))