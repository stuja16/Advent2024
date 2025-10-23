# https://adventofcode.com/2024/day/17

import re

def solve(fileName):
    registers, instructions = open(fileName,"r").read().strip().split("\n\n")
    A,B,C = [int(m) for m in re.findall("-?\d+", registers)]
    instructions = [int(m) for m in re.findall("-?\d+", instructions)]
    instructionPointer = 0
    output = []

    while instructionPointer < len(instructions):
        operand = instructions[instructionPointer+1]      # O(n), but no important since the list is so small
        opcode = instructions[instructionPointer]

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
                output.append(comboOperand % 8)
            case 6:
                B = int(A / (2**comboOperand))
            case 7:
                C = int(A / (2**comboOperand))

        if not opcode == 3:
            instructionPointer += 2

    return ",".join(map(str, output))

#print(solve("Day17/UnitTest1.txt"))
print(solve("Day17/input.txt"))