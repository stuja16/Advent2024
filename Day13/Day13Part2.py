# Must input a correct answer for part 1 before part 2 can be viewed
# https://adventofcode.com/2024/day/13#part2

# All coordinate changes from button presses are positive, so no need to worry about subtraction

# I originally got the idea for the mathematical solution with Cramer's Rule from u/ThunderChaser's post:
# https://www.reddit.com/r/adventofcode/comments/1hd7irq/2024_day_13_an_explanation_of_the_mathematics/

import re

# Offset is passed so I can still run P1 as a test of the new algorithm
def solve(fileName,offset):
    tokens = 0
    # Input cleaning
    for cm in open(fileName,"r").read().strip().split("\n\n"):
        matches = [int(m) for m in re.findall("\d+", cm)]
        tokens += getPresses(matches,offset)

    return tokens

def getPresses(cm,offset) -> int:
    ax,ay,bx,by = cm[:4]
    px,py = [c + offset for c in cm[4:]]

    det = ax*by - ay*bx
    A = (px*by - py*bx) // det  # Double slash divides and rounds the result down
    B = (ax*py - ay*px) // det

    if ax*A+bx*B==px and ay*A+by*B==py:
        return int(3*A+B)
    return 0

print(solve("Day13/UnitTest.txt",0))
print(solve("Day13/input.txt",0))
print(solve("Day13/input.txt",10000000000000))