def threeSum(nums: list[int]) -> list[list[int]]:
    # sort the numbers to use the Two Sum || method
    nums = sorted(nums)
    res=[]

    # set an element as the target 
    for idx, targ in enumerate(nums):
        # take negetive of target ele as adding all the numbers should give us 0
        # rest of the logic is same as Two sum ||
        target = -targ
        # creating a new array by removing the target ele
        numbers = nums[:idx]+nums[idx+1:]
        lp=0
        rp=len(numbers)-1
        while lp<rp:
            # decrement the right pointer, as the list is sorted the only combination of numbers should exist 
            # below(on the left hand side) the rp index
            if numbers[lp]+numbers[rp]>target:
                rp-=1
                continue
            if numbers[lp]+numbers[rp] == target:
                # sort and change type to tuple as set can only be applied on list of tuples and not on list of lists
                # set is applied in the return statement   
                res.append(tuple(sorted([numbers[lp],numbers[rp], targ])))
            lp+=1
            
    return [list(re) for re in set(res)]
    # return list(set(res))

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))

# Runtime
# 9702 ms Beats 5% Memory 653.9 MB Beats 5.22%
