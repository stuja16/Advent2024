# Must input a correct answer for part 1 before part 2 can be viewed
# https://adventofcode.com/2024/day/5#part2

def solve(fileName):
    total = 0   # Final result

    ordering, updates = open(fileName,"r").read().strip().split("\n\n")
    ordering = ordering.split()
    updates = updates.split()
    for o in range(len(ordering)):  # Turns ordering requirements into a list of integer tuples
        ordering[o] = tuple(map(int,ordering[o].split("|")))

    for u in range(len(updates)):   # Checks each update for correct ordering
        total += checkOrdering(ordering, list(map(int,updates[u].split(","))), False)

    return total

# Returns 0 if ordering is incorrect: otherwise, returns middle value
# Function is recursive, changing the first incorrectly ordered pair it finds and before calling itself again
def checkOrdering(ordering, update, changed):
    for o in ordering:
        if o[0] in update and o[1] in update:
            i1 = update.index(o[0])
            i2 = update.index(o[1])
            if i1 >= i2:
                update[i1],update[i2] = update[i2],update[i1]
                return checkOrdering(ordering, update, True)
    return update[int(len(update)/2)] if changed else 0

print(solve("Day5/UnitTest.txt"))
print(solve("Day5/input.txt"))