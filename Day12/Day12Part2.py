# Must input a correct answer for part 1 before part 2 can be viewed
# https://adventofcode.com/2024/day/12#part2

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
        score += len(r) * getSides(r,h,w)
        
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

# Return number of sides for the given region
# Instead of counting sides, it actually counts corners b/c the final total will be the same
def getSides(region,h,w) -> int:
    corners = 0
    for y,x in region:
        for dy in [1,-1]:
            # Check for convex corners
            # Searching by checking every side of every crop in the region. Looking for two adjacent sides with
            # crops from another region or that go beyond the given cropland.
            if y+dy<0 or y+dy>=h or (y+dy,x) not in region:
                for dx in [1,-1]:
                    if x+dx<0 or x+dx>=w or (y,x+dx) not in region:
                        corners += 1
            # Check for concave corners
            # Requires two adjacent sides from the same region, with the diagonal plot btw them from another region.
            elif (y+dy,x) in region:
                for dx in [1,-1]:
                    if x+dx<0 or x+dx>=w: continue
                    if (y,x+dx) in region and (y+dy,x+dx) not in region:
                        corners += 1
                continue

    return corners
    
print(solve("Day12/UnitTest.txt"))
print(solve("Day12/input.txt"))