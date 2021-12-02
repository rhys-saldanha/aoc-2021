from functools import reduce

with open('input.txt', 'r') as inputFile:
    lines = inputFile.readlines()

instructions = list(map(lambda line: line.strip().split(' '), lines))


def sum_instruction_type(instruction_type):
    return reduce(lambda x, y: x + y, map(int,
                                          map(lambda instruction: instruction[1],
                                              filter(lambda instruction: instruction[0] == instruction_type,
                                                     instructions))))


forward = sum_instruction_type('forward')
down = sum_instruction_type('down')
up = sum_instruction_type('up')

depth = down - up

total = forward * depth

print(f"Part 1: {total}")

depth = 0
aim = 0

for instruction in instructions:
    if instruction[0] == 'down':
        aim += int(instruction[1])
    if instruction[0] == 'up':
        aim -= int(instruction[1])
    if instruction[0] == 'forward':
        depth += int(instruction[1]) * aim

total = forward * depth

print(f"Part 2: {total}")