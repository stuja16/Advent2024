# Must input a correct answer for part 1 before part 2 can be viewed
# https://adventofcode.com/2024/day/14#part2

from functools import reduce
import operator
from collections import defaultdict
import re

# Prints the grid for every second < secs
# h&w are the dimensions of the gameboard
def run(fileName: str,h,w,secs):
    robots = [[int(m) for m in re.findall("-?\d+", g)] for g in open(fileName,"r").read().strip().split("\n")]
    for t in range(secs):
        newRobots = [[getNextCord(x,vx,w),getNextCord(y,vy,h),vx,vy] for x,y,vx,vy in robots]
        printGrid(newRobots,h,w)
        robots = newRobots

# Move robot in one cardinal direction for 1 second
def getNextCord(px,vx,size):
    return (px+vx)%size

# Print grid representation of robots in bathroom at the current time
def printGrid(robots,h,w):
    grid = [[0 for _ in range(w)] for _ in range(h)]
    for r in robots:
        x,y,*_ = r
        grid[y][x] += 1
    for r in grid:
        for c in r:
            if c == 0:
                print(" ",end='')
            else:
                print("*",end='')
        print()
    print("--------------------------------------------------------------------")

# Skip from 0s to time t and print the grid at that time
def printGridAtT(fileName,h,w,t):
    robots = [[int(m) for m in re.findall("-?\d+", g)] for g in open(fileName,"r").read().strip().split("\n")]
    finalRobots = [[getFinalCord(px,vx,w,t),getFinalCord(py,vy,h,t),vx,vy] for px,py,vx,vy in robots]
    printGrid(finalRobots,h,w)

# Gets position of the guard after t seconds
def getFinalCord(px,vx,size,t):
    return (px+vx*t)%size

# By stepping through, you can check every grid to find where the robots are the densest
# They form a vertical column at 11s, which will have a periodicity=w=101
# A horizontal column is formed at 65s, which will repeat every 103s (aka h)
# print(run("Day14/input.txt",103,101,103))

# Now I used a free, online calculator to find where these two groups would intersect
# https://www.omnicalculator.com/math/chinese-remainder
timeOfTree = 7687
printGridAtT("Day14/input.txt",103,101,timeOfTree)