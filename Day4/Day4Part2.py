# Must input a correct answer for part 1 before part 2 can be viewed
# https://adventofcode.com/2024/day/4#part2

# Parts of code taken from the following reddit comment solution:
# https://www.reddit.com/r/adventofcode/comments/1h689qf/comment/m0bsh3p/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
# I was unsure how to do this efficiently as my initial idea was just to use regex and rotate the word search repeatedly,
# but I was struggling with the diagonals. The code from u/i_have_no_buscuits provided a more concise solution and taught me
# some new python strategies. I have also adapted it to fit my own general framework.

def solve(fileName):
    lines = open(fileName,"r").readlines()
    h, w = len(lines), len(lines[0])-1  # -1 to account for newline characters
    grid = {(y,x):lines[y][x] for y in range(h) for x in range(w)}

    return findMASes(grid)

def findMASes(grid):
    count = 0
    for y, x in grid:
        if grid[y,x] == "A":
            lr = grid.get((y-1,x-1),"")+grid.get((y+1,x+1),"")  # top-left & bot-right
            rl = grid.get((y+1,x-1),"")+grid.get((y-1,x+1),"")  # top-right & bot-left
            count += (lr in {"MS", "SM"}) and (rl in {"MS", "SM"})  # Both diagonals must be "MAS"
    return count

print(solve("Day4/UnitTest.txt"))
print(solve("Day4/input.txt"))