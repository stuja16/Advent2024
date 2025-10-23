# Must input a correct answer for part 1 before part 2 can be viewed
# https://adventofcode.com/2024/day/19#part2

# Takes a few seconds to run
# Could obvi be optimized, but it's fast enough for me

def solve(fileName):
    availableTowels, desiredPatterns = open(fileName,"r").read().strip().split("\n\n")
    availableTowels = availableTowels.split(", ")
    desiredPatterns = desiredPatterns.split("\n")

    count = 0

    for desiredPattern in desiredPatterns:
        count += checkPattern(desiredPattern,availableTowels)

    return count

def checkPattern(desiredPattern, availableTowels):
    foundPatterns = [["",1]]    # Combination frequency table & queue
    count = 0

    while foundPatterns:
        # If successful path found, add to score
        if foundPatterns[0][0] == desiredPattern:
            count += foundPatterns[0][1]
        # Else search for more paths
        elif len(foundPatterns[0][0]) < len(desiredPattern):
            for towel in availableTowels:
                testPattern = foundPatterns[0][0]+towel

                if desiredPattern.find(testPattern) == 0:
                    # Check if pattern is a repeat
                    repeat = False
                    for i in range(len(foundPatterns)):
                        if testPattern == foundPatterns[i][0]:
                            foundPatterns[i][1] += foundPatterns[0][1]
                            repeat = True
                            break
                    if not repeat:
                        foundPatterns.append([testPattern,foundPatterns[0][1]])

        foundPatterns = foundPatterns[1:]
    return count

print(solve("Day19/UnitTest.txt"))
print(solve("Day19/input.txt"))