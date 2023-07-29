# Time complexity: O(n)
# Space complexity: O(1)
# Runtime: Beats 98.66% | Memory: Beats 72.04%

"""
Moore's Voting Algorithm:
This will work only if the following condition satisfies, "The majority element is the element that appears more than ⌊n / 2⌋ times."
Here, you take an element and increment the counter as you find similar ele and decrement if you find dissimilar elements. 
And if the above condition satifies, at the end of it you'll have Majority element.
"""
def majorityElement(nums: list[int]) -> int:
    count, res = 0,0

    for i in nums:
        if count == 0:
            res = i

        if res == i:
            count+=1
        else:
            count-=1

    return res

nums = [2,2,1,1,1,2,2]
print(majorityElement(nums))

# ------------------- HASHMAP APPROACH ----------------- #

# Time complexity: O(n) : cause 2 seperate for loops
# Space complexity: O(n): cause creating a dictionary 
# Runtime: Beats 99.67% | Memory: Beats 72.4%

def majorityElement_1(nums: list[int]) -> int:
    count = {}
    counter = -1
    key = -1
    for i in nums:
        count[i] = count.get(i, 0) + 1

    for key, val in count.items():
        if val > counter:
            counter = val
            res = key

    return res

# nums = [2,2,1,1,1,2,2]
# print(majorityElement(nums))
