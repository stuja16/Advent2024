# https://adventofcode.com/2024/day/5

def solve(fileName):
    total = 0   # Final result

    ordering, updates = open(fileName,"r").read().strip().split("\n\n")
    ordering = ordering.split()
    updates = updates.split()
    for o in range(len(ordering)):  # Turns ordering requirements into a list of integer tuples
        ordering[o] = tuple(map(int,ordering[o].split("|")))

    for u in range(len(updates)):   # Checks each update for correct ordering
        total += checkOrdering(ordering, list(map(int,updates[u].split(","))))

    return total

# Returns 0 if ordering is incorrect: otherwise, returns middle value
def checkOrdering(ordering, update):
    for o in ordering:
        if o[0] in update and o[1] in update:
            if update.index(o[0]) >= update.index(o[1]):
                return 0
    return update[int(len(update)/2)]

print(solve("Day5/UnitTest.txt"))
print(solve("Day5/input.txt"))