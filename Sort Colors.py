# Time complexity O(n): Every iteration of while loop, one element gets sorted 
# Memory O(1)
# Runtime: Beats 73.85% | Memory: Beats 73.38%

"""
Dutch National FLag Algorithm:
Here we assume that a list is divided in 4 parts, and 3 parts of it are sorted. If 'a' is an array.

a[0] to a[low-1]    : contains only 0's    -> Sorted part of array
a[low] to a[mid-1]  : contains only 1's     -> Sorted part of array
a[mid] to a[high-1] : is an unsorted array  -> Un-sorted part of array
a[high] to a[n]     : contains only 2's     -> Sorted part of array

"""
def sortColors(nums: list[int]) -> None:
    l = 0 #low
    m = 0 #mid
    h = len(nums)-1 #high

    while m<=h:

        if nums[m]==0:
            temp = nums[l]
            nums[l] = nums[m]
            nums[m] = temp
            l+=1
            m+=1

        # should be an elif condition, not an if. 
        elif nums[m] == 1:
            m+=1

        elif nums[m] == 2:
            temp = nums[h]
            nums[h] = nums[m]
            nums[m] = temp
            h-=1

    return nums

nums = [2,0,1]
print(sortColors(nums))

# ------------------- BRUTE FORCE APPROACH ----------------- #

# Time complexity O(n2): 2 for loops
# Memory O(1)
# Runtime: Beats 6.93% | Memory: Beats 73.38%
def sortColors_1(nums: list[int]) -> None:

    for i in range(len(nums)):
        for j in range(len(nums)-1):
            if nums[j] > nums[j+1]:
                temp = nums[j+1]
                nums[j+1] = nums[j]
                nums[j] = temp
    return nums

# nums = [2,0,2,1,1,0]
# print(sortColors(nums))