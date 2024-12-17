# https://adventofcode.com/2024/day/11

# Takes a few seconds to run, could be optimized more
# Oh look, P2 is just an optimized version of P1

def solve(fileName,blinks):
    stones = list(map(int,open(fileName,"r").read().strip().split(" ")))

    for i in range(blinks):
        stones = blink(stones)

    return len(stones)

def blink(stones):
    newStones = []

    while stones:
        s = stones.pop(0)
        if not s:
            newStones.append(1)
        elif not len(str(s))%2:
            si = int(len(str(s))/2)
            newStones.append(int(str(s)[:si]))
            newStones.append(int(str(s)[si:]))
        else:
            newStones.append(s*2024)

    return newStones
    
print(solve("Day11/UnitTest.txt",6))
print(solve("Day11/UnitTest.txt",25))
print(solve("Day11/input.txt",25))