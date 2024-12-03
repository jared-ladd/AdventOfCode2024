import re

file = open("input.txt" ,"r")

program = file.read()

part1muls = re.findall(r"mul\([0-9]+,[0-9]+\)", program)

## TODO: learn regex
part2operations = re.findall(r"(mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\))", program)

def getProduct(operation):
    operation = operation.replace('mul(', '')
    operation = operation.replace(')', '')
    nums = [int(x) for x in operation.split(",")]
    return nums[0] * nums[1]


part1 = 0
for operation in part1muls:
    part1 += getProduct(operation)

print(f'Part 1: {part1}')

part2 = 0
mostRecent = "do()"
for op in part2operations:
    if op == "do()" or op == "don't()":
        mostRecent = op
    elif mostRecent == 'do()':
        part2 += getProduct(op)

print(f'Part 2: {part2}')


