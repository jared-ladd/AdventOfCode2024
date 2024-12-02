file = open("input.txt", "r")

left_list = []
right_list = []

for line in file:
    nums = line.split("   ")
    left_list.append(int(nums[0]))
    right_list.append(int(nums[1]))

left_list.sort()
right_list.sort()

right_dict = {}

for el in right_list:
    if el in right_dict:
        right_dict[el] += 1
    else:
        right_dict[el] = 1

res = 0
for el in left_list:
    if el in right_dict:
        res += el * right_dict[el]
        
print(res)