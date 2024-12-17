# Must input a correct answer for part 1 before part 2 can be viewed
# https://adventofcode.com/2024/day/9#part2

def solve(fileName):
    nums = list(map(int,open(fileName,"r").read().strip()))
    storage = []

    # Create a list of all files and empty spaces. Spaces are given a value of -1
    index = 0
    for i,n in enumerate(nums):
        if n == 0:  # Ignore sections with no size: AKA just there for input formatting
            continue

        if not i%2:
            storage.append((int(i/2),index,n))
        else:
            storage.append((-1,index,n))
        index += n
    storage = storage[1:]   # 1st file always has a score of 0 & can't be moved

    return compactStorage(storage)

# Takes a storage window and compacts it while finding the sum score
# Changed from recursive to iterative b/c it had too many function calls
def compactStorage(store):
    score = 0
    
    while store:
        # Trim files from the start of our storage window: They can't be moved any closer
        while True:
            if not store:   # If this loop removes the last remaining files, escape
                return score
            elif store[0][0] != -1:
                score += getScore(store[0][0],store[0][1],store[0][2])
                store.pop(0)
            else:
                break

        # Trim spaces from the end of the storage window: There's nothing further to fill them with 
        while True:
            if not store:   # If this loop removes the last remaining files, escape
                return score
            elif store[len(store)-1][0] == -1:
                store.pop()
            else:
                break

        # Try to move the last remaining file in the current window
        nextFile = store.pop()
        score += moveFile(store, nextFile)

    return score

# Tries to move the given file into the given storage window which represents part of the file storage to the left
# Then returns the file's score whether it can be moved or not
def moveFile(store, file):
    score = 0
    num,i,freq = file
    for s,(n2,i2,f2) in enumerate(store):
        if n2 == -1 and f2 == freq:     # If exactly the right amount of space is found
            score += getScore(num,i2,freq)
            store.pop(s)
            break
        elif n2 == -1 and f2 > freq:    # If extra space is found
            score += getScore(num,i2,freq)
            store.pop(s)
            newFreq = f2 - freq
            newIndex = i2 + freq
            store.insert(s, (-1,newIndex,newFreq))
            break

    # If the whole list is checked and no spaces are found.
    if not score:
        return getScore(*file)

    return score

def getScore(n,i,f):
    score = 0
    for j in range(f):
        score += (i+j) * n
    return score

print(solve("Day9/UnitTest.txt"))
print(solve("Day9/input.txt"))