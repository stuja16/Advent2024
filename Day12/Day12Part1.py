# https://adventofcode.com/2024/day/12

def solve(fileName):
    lines = open(fileName,"r").readlines()
    h, w = len(lines), len(lines[0])-1  # -1 to account for newline characters
    grid = {(y,x):lines[y][x] for y in range(h) for x in range(w)}

    regions = []
    visited = set()
    
    for y,x in grid:
        if (y,x) in visited: continue
        visited.add((y,x))

        region = {(y,x)}
        findRegion(y,x,grid,h,w,visited,region)
        regions.append(region)

    # Find the price
    score = 0
    for r in regions:
        score += len(r) * getPerimeter(r)
        
    return score

# No return value b/c the coords for the region are added to the "region" set parameter
def findRegion(y,x,grid,h,w,visited,region) -> None:
    # Check to the right and below
    for dy,dx in [(0,1),(1,0),(-1,0),(0,-1)]:
        ny,nx = y+dy,x+dx
        if 0>ny or ny>=h or 0>nx or nx>=w: continue
        if grid[ny,nx] == grid[y,x] and not (ny,nx) in visited:
            visited.add((ny,nx))
            region.add((ny,nx))
            findRegion(ny,nx,grid,h,w,visited,region)

# Return perimeter for the given region
def getPerimeter(region) -> int:
    # Every square has 4 sides, except where they touch others in the same region
    perimeter = len(region) * 4
    for c in region:
        for dy,dx in [(0,1),(1,0),(-1,0),(0,-1)]:
            ny,nx = c[0]+dy,c[1]+dx
            if (ny,nx) in region:
                perimeter -= 1

    return perimeter
    
print(solve("Day12/UnitTest.txt"))
print(solve("Day12/input.txt"))