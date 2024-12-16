# https://adventofcode.com/2024/day/2

def solve(fileName):
    sum = 0

    lines = open(fileName,"r").read().strip().split('\n')   # Read input data, split on whitespace since there are 2 numbers per line
    for l in lines:
        line = l.split()
        if isSafe(list(map(int,line))):
            sum += 1

    return sum

# Determines if the provided report is safe based on given criteria
# Returns boolean True if report is safe, v.v.
def isSafe(report):
    increasing = True
    for n in range(len(report)-1):  # We're searching pairs, not individual elements
        e1 = report[n]
        e2 = report[n+1]
        if n != 0:  # Different actions for the first pair
            if e1 > e2 and increasing:
                return False
            elif e2 > e1 and not increasing:
                return False
        else:
            if e1 > e2:
                increasing = False
        
        # Need to check magnitude for all pairs
        if abs(e1 - e2) > 3 or e1 == e2:
            return False
    
    # If all checks were passed without failue conditions activated, the report must be valid
    return True


print(solve("Day2/UnitTest.txt"))
print(solve("Day2/input.txt"))