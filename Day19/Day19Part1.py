# https://adventofcode.com/2024/day/19

from collections import deque

def solve(fileName):
    availableTowels, desiredPatterns = open(fileName,"r").read().strip().split("\n\n")
    availableTowels = availableTowels.split(", ")
    desiredPatterns = desiredPatterns.split("\n")

    count = 0

    for desiredPattern in desiredPatterns:
        count += checkPattern(desiredPattern,availableTowels)

    return count

def checkPattern(desiredPattern, availableTowels):
    possiblePatterns = deque()      # List of current attempts to make desired pattern
    possiblePatterns.append("")
    foundPatterns = []

    while possiblePatterns:
        pattern = possiblePatterns.popleft()

        for towel in availableTowels:
            testPattern = pattern+towel
            if desiredPattern == testPattern:
                return 1
            elif testPattern not in foundPatterns and desiredPattern.find(testPattern) == 0:
                possiblePatterns.append(testPattern)
                foundPatterns.append(testPattern)

    return 0

print(solve("Day19/UnitTest.txt"))
print(solve("Day19/input.txt"))