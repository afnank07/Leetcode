# Brute force approach
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]



# Dictionary approach
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        holder = {}
        for i, num in enumerate(nums):
            num2 = target - num
            if num2 in holder:
                return [holder[num2], i]
            else:
                holder[num] = i
                