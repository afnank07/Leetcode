# Time complexity: O(n)
# Space complexity: O(1)
# Runtime: Beats 90.81% | Memory: Beats 68.22%

"""
Moore's Voting Algorithm: Extended
This version of Moore's Voting Algorithm is for the elements that appears more than ⌊n / 3⌋ times.
It's the same strategy as for [n/2], but now you have 2 counters and elements.
"""

def majorityElement(nums: list[int]) -> list[int]:
    cnt1, cnt2 = 0,0
    ele1, ele2 = None, None
    res = []

    for i in nums:

        if cnt1 == 0 and i != ele2:
            cnt1 += 1
            ele1 = i
        elif cnt2 == 0 and i != ele1:
            cnt2 += 1
            ele2 = i
        elif i == ele1:
            cnt1 += 1
        elif i == ele2:
            cnt2 += 1
        else: 
            cnt1 -= 1
            cnt2 -= 1

    cnt1, cnt2 = 0, 0
    maxCount = int(len(nums)/3)

    for i in nums:
        if i == ele1: cnt1 += 1
        if i == ele2: cnt2 += 1

    if cnt1 > maxCount: res.append(ele1)
    if cnt2 > maxCount: res.append(ele2)

    return res

# nums = [3,2,3]
# nums = [1]
# nums = [1,2]
# nums = [1,2,3]
nums = [3,2,2,2,3]
print(majorityElement(nums))

# ------------------- SECOND APPROACH ----------------- #

# Time complexity: O(n)
# Space complexity: O(n)
# Runtime: Beats 99.55% | Memory: Beats 95.16%

"""
Give all the elements that are > [n/3]
"""
def majorityElement_1(nums: list[int]) -> list[int]:
    counter = {}
    res = []

    for i in nums:
        counter[i] = counter.get(i, 0) + 1

    for key, val in counter.items():
        if val > int(len(nums) / 3):
            res.append(key)

    return res

# nums = [3,2,3]
# nums = [1]
# nums = [1,2]
# nums = [1,2,3]
# nums = [3,2,2,2,3]
# print(majorityElement(nums))