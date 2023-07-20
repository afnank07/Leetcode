# Kadanes Algorithm
# Time complexity O(n): Just 1 loop
# Space complexity: O(1)
# Runtime: Beats 85.78% | Memory: Beats 91.30%

"""
Intuition: -ve sum is dropped and if entire input list is of -ve numbers then only the lowest -ve number is stored as sum.
"""
def maxSubArray(nums: list[int]) -> int:
    maxSum = nums[0]
    curSum = 0
    for n in nums:
        if curSum < 0:
            curSum = 0
        curSum += n
        maxSum = max(maxSum, curSum)
    return maxSum

nums = [-2, -1, -1, -2]
print(maxSubArray(nums))

# ------------------- OTHER APPROACHES ----------------- #

# Brute Force approach 
# Time complexity O(n3): 2 seperate loops and sum is O(n)
# Space complexity: O(1)
def maxSubArray(nums: list[int]) -> int:
    lp=0
    total = -1

    for lp in range(len(nums)):
        rp=len(nums)
        while lp<rp:
            new_total = sum(nums[lp:rp])
            print(nums[lp:rp])
            
            if total < new_total:
                total = new_total
                print("total: ", total)
                f_lp, f_rp = lp, rp
            rp-=1
 
    return total

# nums = [-1, -1, -2]
# print(maxSubArray(nums))