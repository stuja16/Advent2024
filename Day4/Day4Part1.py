# https://adventofcode.com/2024/day/4

# Parts of code taken from the following reddit comment solution:
# https://www.reddit.com/r/adventofcode/comments/1h689qf/comment/m0bsh3p/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
# I was unsure how to do this efficiently as my initial idea was just to use regex and rotate the word search repeatedly,
# but I was struggling with the diagonals. The code from u/i_have_no_buscuits provided a more concise solution and taught me
# some new python strategies. I have also adapted it to fit my own general framework.

def solve(fileName):
    lines = open(fileName,"r").readlines()
    h, w = len(lines), len(lines[0])-1  # -1 to account for newline characters
    grid = {(y,x):lines[y][x] for y in range(h) for x in range(w)}
    target = "XMAS"

    return findTargets(grid,target)

def findTargets(grid, target):
    DELTAS = [(dy,dx) for dy in [-1,0,1] for dx in [-1,0,1] if (dx!=0 or dy!=0)]
    count = 0
    for y, x in grid:
        for dy,dx in DELTAS:
            candidate = "".join(grid.get((y+dy*i, x+dx*i),"") for i in range(len(target)))
            count += candidate == target
    return count

print(solve("Day4/UnitTest.txt"))
print(solve("Day4/input.txt"))