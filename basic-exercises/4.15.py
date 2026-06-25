"""
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 8, 5, 6, 3, 2, 1, 2]
nums_copy = nums.copy()
nums_copy.reverse()
result = len(nums_copy) - 1 - nums_copy.index(1)
print(result)

"""


"""
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 8, 5, 6, 3, 2, 1, 2]
count = nums.count(8)
length = len(nums)
for each in range(length):
    if nums[each] == 8:
        count -= 1
    if count == 0:
        print(each)
        break
"""


"""
nums = [2, 2, 4, 2, 3, 6, 2]
nums.sort()
length = len(nums)
half = nums[length // 2]
count = 0

for each in nums:
    if each == half:
        count += 1
if count > length/2:
    print("存在主要元素，是",half)
else:
    print("不存在主要元素！")
"""

nums = [2, 2, 4, 2, 3, 6, 2]
major = nums[0]
count = 0
for each in nums:
    if count == 0:
        major = each
    if each == major:
        count += 1
    else:
        count -= 1
if nums.count(major) > len(nums) / 2:
    print("主要元素是:",major)
else:
    print("不存在主要元素。")
