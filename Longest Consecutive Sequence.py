
def longestConsecutive(nums):
    if len(nums) == 0:
        return 0
    
    nums = sorted(set(nums))
    print(nums)
    lp = 0
    count = 1
    bestcount = 1

    for rp in range(1, len(nums)):
        if ((nums[rp] - nums[lp]) == 1):
            count +=1
        else:
            count=1

        # print("count: ", count)
        # print("nums[lp] - nums[rp]: ", nums[lp] - nums[rp])
        if bestcount < count:
            bestcount = count

        lp+=1

    return bestcount

nums = [100,4,200,1,3,2]
print(longestConsecutive(nums))