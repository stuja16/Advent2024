# Must input a correct answer for part 1 before part 2 can be viewed
# https://adventofcode.com/2024/day/16#part2
# Solved with Djikstra's algorithm

from heapq import heappop, heappush

def solve(fileName):
    grid = [list(x) for x in open(fileName,"r").read().strip().split("\n")]

    startPos = (len(grid)-2,1)
    startDir = (0,1)
    minScore = 160624
    bestTiles = set()   # Will contain ALL squares that are part of ANY shortest path
    visited = {}        # The minimum cost to every position
    visited[*startPos,*startDir] = 0

    # Setup data structures for djikstra
    pq = []             # Min queue of valid ways to continue the path
    heappush(pq,(0,(startPos,startDir,{startPos})))

    # Cull thread if a shorter path has already been found
    def isShortestPath(y,x,dy,dx,score):
        bestScore = visited.get((y,x,dy,dx))
        if bestScore and bestScore < score:
            return False
        visited[(y,x,dy,dx)] = score
        return True

    # Run djikstra
    while pq:
        curScore, ((y,x),(dy,dx),path) = heappop(pq)

        # Skip if path is longer than shortest already found
        if curScore > minScore:
            continue

        # Complete path if end reached
        if grid[y][x] == "E":
            if curScore < minScore:
                minScore = curScore
                bestTiles = set()
                bestTiles.update(path)
            elif curScore == minScore:
                bestTiles.update(path)
            continue

        # Check if we've already found a shorter path to this location
        if not isShortestPath(y,x,dy,dx,curScore):
            continue

        # Branch out in forward direction:
        nextPos = (y+dy,x+dx)
        if nextPos not in path and not grid[y+dy][x+dx] == "#":
            heappush(pq,(curScore+1,(nextPos,(dy,dx),path | {(nextPos)})))

        # If moving E or W, check N/S
        if dy == 0:
            dy,dx = 1,0
            nextPos = (y+dy,x+dx)
            if nextPos not in path and not grid[y+dy][x+dx] == "#":
                heappush(pq,(curScore+1001,(nextPos,(dy,dx),path | {(nextPos)})))
            dy,dx = -1,0
            nextPos = (y+dy,x+dx)
            if nextPos not in path and not grid[y+dy][x+dx] == "#":
                heappush(pq,(curScore+1001,(nextPos,(dy,dx),path | {(nextPos)})))
        else:   # Check E/W
            dy,dx = 0,1
            nextPos = (y+dy,x+dx)
            if nextPos not in path and not grid[y+dy][x+dx] == "#":
                heappush(pq,(curScore+1001,(nextPos,(dy,dx),path | {(nextPos)})))
            dy,dx = 0,-1
            nextPos = (y+dy,x+dx)
            if nextPos not in path and not grid[y+dy][x+dx] == "#":
                heappush(pq,(curScore+1001,(nextPos,(dy,dx),path | {(nextPos)})))

    return len(bestTiles)

print(solve("Day16/UnitTest.txt"))
print(solve("Day16/input.txt"))