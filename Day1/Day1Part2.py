# Must input a correct answer for part 1 before part 2 can be viewed
# https://adventofcode.com/2024/day/1#part2

from collections import Counter

def solve(fileName):
    lines = open(fileName,"r").read().strip().split()   # Read input data, split on whitespace since there are 2 numbers per line
    numbers = list(map(int,lines))  # Convert from strings to integers for math operations

    # Split list into two based on odds and evens to account for the two columns in the input
    list1, list2 = ([] for i in range(2))
    for n, num in enumerate(numbers):
        if n%2==0:
            list1.append(num)
        else:
            list2.append(num)

    # Create a frequency table for integers in the 2nd list to prevent the need to search the entire list repeatedly
    freq = Counter(list2)
    return calculateSimilarityScore(list1,freq)

# Inputs one list and a frequency table of the other to calculate requested score
def calculateSimilarityScore(list,freq):
    sum = 0 # Final answer variable
    for num in list:
        sum += num * freq[num]
    
    return sum


print(solve("Day1/UnitTest.txt"))
print(solve("Day1/input.txt"))