# Must input a correct answer for part 1 before part 2 can be viewed
# https://adventofcode.com/2024/day/17#part2

# Key observations:
#     - A is the only register that matters
#     - If A is written in octal, the ones digit is what produces the 1st output
#     - For every subsequent output, the program discards the one's place and moves all digits to the right
#     - Thus, we can construct the value of A one octal digit at a time
#     - Bc of the structure of the program, multiple values will work, so we must consider all candidates

import re

def solve(fileName):
    global INSTRUCTIONS, A,B,C, OUTPUT
    _, INSTRUCTIONS = open(fileName,"r").read().strip().split("\n\n")
    INSTRUCTIONS = [int(m) for m in re.findall("-?\d+", INSTRUCTIONS)]
    OUTPUT = []

    possibleAs = {0}

    for i in range(len(INSTRUCTIONS)):
        targetInstruction = INSTRUCTIONS[-(i+1)]

        for posA in possibleAs.copy():
            possibleAs.remove(posA)

            posA *= 8      # Shift one place to the left in octal so we can try the next digit

            for aOnesPlace in range(8):
                OUTPUT.clear()
                A = posA + aOnesPlace
                B = 0
                C = 0
                runProgram()

                if OUTPUT and OUTPUT[0] == targetInstruction:
                    possibleAs.add(posA+aOnesPlace)

    return min(possibleAs)

# Runs program on 3-bit computer from input file
def runProgram():
    global INSTRUCTIONS, A,B,C, OUTPUT
    instructionPointer = 0

    while instructionPointer < len(INSTRUCTIONS):
        operand = INSTRUCTIONS[instructionPointer+1]      # O(n), but no important since the list is so small
        opcode = INSTRUCTIONS[instructionPointer]

        match operand:
            case 6:
                comboOperand = C
            case 5:
                comboOperand = B
            case 4:
                comboOperand = A
            case _:
                comboOperand = operand

        match opcode:
            case 0:
                A = int(A / (2**comboOperand))
            case 1:
                B = B ^ operand     # Bitwise XOR
            case 2:
                B = comboOperand % 8
            case 3:
                if A == 0:
                    instructionPointer += 2
                    continue
                instructionPointer = operand
            case 4:
                B = B ^ C           # Bitwise XOR
            case 5:
                OUTPUT.append(comboOperand % 8)
            case 6:
                B = int(A / (2**comboOperand))
            case 7:
                C = int(A / (2**comboOperand))

        if not opcode == 3:
            instructionPointer += 2

    return

print(solve("Day17/UnitTest2.txt"))
print(solve("Day17/input.txt"))