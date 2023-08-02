
def reversePairs(nums: list[int]) -> int:
    count = 0
    for lp in range(len(nums)):
        rp = len(nums)-1
        while lp < rp:
            if nums[lp] > 2 * nums[rp]:
                count += 1
            rp -= 1
    return count

nums = [1,3,2,3,1]
nums = [2,4,3,5,1]
print(reversePairs(nums))

# ------------------- BRUTE FORCE - TIME LIMIT EXCEEDED ----------------- #

def reversePairs_2(nums: list[int]) -> int:
    count = 0
    for lp in range(len(nums)):
        rp = len(nums)-1
        while lp < rp:
            if nums[lp] > 2 * nums[rp]:
                count += 1
            rp -= 1
    return count

# nums = [1,3,2,3,1]
# print(reversePairs(nums))

# ------------------- BRUTE FORCE - TIME LIMIT EXCEEDED ----------------- #

def reversePairs_1(nums: list[int]) -> int:
    count = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i < j:
                if nums[i] > 2 * nums[j]:
                    count+=1
    return count

# nums = [1,3,2,3,1]
# print(reversePairs(nums))