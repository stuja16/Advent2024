# https://adventofcode.com/2024/day/14

from functools import reduce
import operator
from collections import defaultdict
import re

# h&w are the dimensions of the gameboard, & secs is the amount of seconds of movement to simulate
def solve(fileName,h,w,secs):
    quadrants = defaultdict(int)
    mx,my = int(w/2),int(h/2)

    for g in open(fileName,"r").read().strip().split("\n"):
        px,py,vx,vy = [int(m) for m in re.findall("-?\d+", g)]
        fx,fy = getFinalP(px,py,vx,vy,h,w,secs)
        if fx>mx and fy>my:
            quadrants[1] += 1
        elif mx>fx and fy>my:
            quadrants[2] += 1
        elif mx>fx and my>fy:
            quadrants[3] += 1
        elif fx>mx and my>fy:
            quadrants[4] += 1

    return reduce(operator.mul,[quadrants[i] for i in range(1,5)],1)

# Gets position of the guard after t seconds
def getFinalP(px,py,vx,vy,h,w,t):
    x,y = px+vx*t,py+vy*t
    return x%w,y%h

print(solve("Day14/UnitTest.txt",7,11,100))
print(solve("Day14/input.txt",103,101,100))