file = open("input.txt", "r")

def LevelIsSafe(nums):
    safe = True
    increasing = (nums[-1] - nums[0]) > 0
    for i in range(len(nums) - 1):
        if increasing:
            diff = nums[i+1] - nums[i]
            if diff > 3 or diff < 1:
                safe = False
        else:
            diff = nums[i] - nums[i+1]
            if diff > 3 or diff < 1:
                safe = False
    return safe
    
part1 = 0
part2 = 0
for line in file:
    nums = line.split()
    nums = [int(num) for num in nums]
    if LevelIsSafe(nums):
        part1 += 1
    for i in range(len(nums)):
        temp = nums.copy()
        temp.pop(i)
        if LevelIsSafe(temp):
            part2 += 1
            break


print(f'Part 1 solution: {part1}')
print(f'Part 2 solution: {part2}')


