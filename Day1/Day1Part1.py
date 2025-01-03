# https://adventofcode.com/2024/day/1

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
    return findDifference(list1,list2)

# Takes two numeric, positive lists and finds the sum of the differences between each element once sorted by magnitude
def findDifference(list1,list2):
    list1.sort()
    list2.sort()

    sum = 0
    for n, num in enumerate(list1):
        sum += abs(num-list2[n])
    
    return sum


print(solve("Day1/UnitTest.txt"))
print(solve("Day1/input.txt"))