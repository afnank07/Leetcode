# Time complexity: O(n)
# Space complexity: O(1): inplace
# Runtime: Beats 56.54% | Memory: Beats 51.6%

"""
Floyd's Algorithm or Tortoise Hare Method:

It's a linked list based method, where you start 2 pointers from 0th index.

Cycle 1:
Slow pointer moves 1 step at a time, traversing the list by considering the number it finds in index 0 as an index itself.
Fast pointer moves 2 steps at a time.
The cycle ends when slow pointer and fast ponter points towards the same number. 

Cycle 2:
Slow pointer moves 1 step at a time, from the previous cycle's location.
Fast pointer also moves 1 step at a time starting from 0th index again.
The cycle ends when slow pointer and fast ponter points towards the same number. And this is the answer.

Watch: https://www.youtube.com/watch?v=32Ll35mhWg0

"""
def findDuplicate(nums: list[int]) -> int:
    slow = 0
    fast = 0

    # First Cycle
    while True:
        # 1 step at a time for slow pointer 
        slow = nums[slow]
        # 2 steps at a time for fast pointer 
        fast = nums[nums[fast]]

        if slow == fast:
            break

    # Second Cycle
    fast = 0
    while True:
        # In second cycle both the pointers move at same speed
        slow = nums[slow]
        fast = nums[fast]

        if slow == fast:
            return slow

# nums = [1,3,4,2,2]
nums = [3,1,3,4,2]
print(findDuplicate(nums))

# ------------------- SORT APPROACH ----------------- #

def findDuplicate_2(nums: list[int]) -> int:
    nums.sort()

    for i in range(1, len(nums)):
        if nums[i-1] == nums[i]:
            return nums[i]

# nums = [1,3,4,2,2]
# print(findDuplicate(nums))

# ------------------- BRUTE FORCE APPROACH ----------------- #

# Time limit exceeded
def findDuplicate_1(nums: list[int]) -> int:
    for idx, i in enumerate(nums):
        if i in (nums[:idx] + nums[idx+1:]):
            return i

    return 

# nums = [1,3,4,2,2]
# print(findDuplicate(nums))