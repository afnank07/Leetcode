# Brute force approach
def twoSum(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] == target:
                return [i,j]

# ------------------- SECOND APPROACH ----------------- #

# Dictionary approach
def twoSum(nums: list[int], target: int) -> list[int]:
    holder = {}
    for i, num in enumerate(nums):
        num2 = target - num
        if num2 in holder:
            return [holder[num2], i]
        else:
            holder[num] = i
                