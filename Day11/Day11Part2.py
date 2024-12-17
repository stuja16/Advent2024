# Must input a correct answer for part 1 before part 2 can be viewed
# https://adventofcode.com/2024/day/11#part2

# Originally I tried modifying the list in place, but that had no significant change in its speed
# Then, took inspiration from the following comment thread for final solution:
# https://www.reddit.com/r/adventofcode/comments/1hbmu6q/comment/m1hsgae/

from collections import defaultdict

def solve(fileName,blinks):
    # Using a dictionary instead of a list allows us to do calculations for identical stones in one operation
    # The defaultdict structure is like a dict, but you can alter non-existent entries w/o error b/c it gives a default
    # value of 0 for ints.
    stones = defaultdict(int)
    for x in open(fileName,"r").read().strip().split(" "):
        stones[int(x)] += 1

    for i in range(blinks):
        print("Blink: ",i)
        stones = blink(stones)

    score = 0
    for s in stones:
        score += stones[s]
    return score

def blink(stones):
    newStones = defaultdict(int)

    for s in stones:
        if not s:
            newStones[1] += stones[0]
        elif not len(str(s))%2:
            si = int(len(str(s))/2)
            newStones[int(str(s)[:si])] += stones[s]
            newStones[int(str(s)[si:])] += stones[s]
        else:
            newStones[s*2024] += stones[s]
    
    return newStones

print(solve("Day11/UnitTest.txt",25))
print(solve("Day11/input.txt",75))