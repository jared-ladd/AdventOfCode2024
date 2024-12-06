file = open("input.txt", "r")

lines = []
for line in file:
    lines.append(line.strip())

empty_line = lines.index('')

rules = [line.split("|") for line in lines[:empty_line]]
updates = [line.split(",") for line in lines[empty_line+1:]]

def checkRules(update):
    for rule in rules:
        if rule[0] not in update or rule[1] not in update:
            continue
        if update.index(rule[0]) > update.index(rule[1]):
            return False
    return True

def swapOnBrokenRules(update):
    for rule in rules:
        if rule[0] not in update or rule[1] not in update:
            continue
        left = update.index(rule[0])
        right = update.index(rule[1])
        if left > right:
            tmp = update[left]
            update[left] = update[right]
            update[right] = tmp

part1total = 0
part2total = 0
for update in updates:
    if checkRules(update):
        part1total += int(update[len(update) // 2])
    else:
        while not checkRules(update):
            swapOnBrokenRules(update)
        part2total += int(update[len(update) // 2])

print(f'Part 1 total: {part1total}')
print(f'Part 2 total: {part2total}')
