# https://adventofcode.com/2024/day/9

def solve(fileName):
    sum = 0

    nums = list(map(int,open(fileName,"r").read().strip()))
    files = {}
    maxFile = int()

    # Create a dictionary of all files: key=index, value=frequency
    for i,n in enumerate(nums):
        if not i%2:
            files[int(i/2)] = n
            maxFile = int(i/2)

    index = 0
    for i,n in enumerate(nums):
        # If no files are left, we already have the final total
        if not files:
            break

        if not i%2:
            for j in range(files[int(i/2)]):
                sum += (index+j) * int(i/2)
            del files[int(i/2)]
        else:
            # When coming upon an empty space, fill it in and add to the checksum
            # "n" is the number of spaces to fill
            sum, maxFile = fillSpace(index, n, files, sum, maxFile)
        index += n

    return sum

def fillSpace(index, spaces, files, sum, max):
    if spaces <= files[max]:
        for s in range(spaces):
            sum += (index+s) * max
            
        files[max] -= spaces

        if files[max] == 0:
            del files[max]
            max -= 1
    else:
        for s in range(files[max]):
            sum += (index+s) * max
        
        spaces -= files[max]
        newIndex = index + files[max]
        del files[max]
        max -= 1
        sum, max = fillSpace(newIndex, spaces, files, sum, max)   # Recursive call to fill remaining space
    return (sum, max)
    
print(solve("Day9/UnitTest.txt"))
print(solve("Day9/input.txt"))