# Runtime
# 9702 ms Beats 5% Memory 653.9 MB Beats 5.22%

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

# ------------------- SECOND APPROACH ----------------- #

# Another faster approach beats 97%
def threeSum_2(self, nums: list[int]) -> list[list[int]]:
	res = set()

	#1. Split nums into three lists: negative numbers, positive numbers, and zeros
	n, p, z = [], [], []
	for num in nums:
		if num > 0:
			p.append(num)
		elif num < 0: 
			n.append(num)
		else:
			z.append(num)

	#2. Create a separate set for negatives and positives for O(1) look-up times
	N, P = set(n), set(p)

	#3. If there is at least 1 zero in the list, add all cases where -num exists in N and num exists in P
	#   i.e. (-3, 0, 3) = 0
	if z:
		for num in P:
			if -1*num in N:
				res.add((-1*num, 0, num))

	#3. If there are at least 3 zeros in the list then also include (0, 0, 0) = 0
	if len(z) >= 3:
		res.add((0,0,0))

	#4. For all pairs of negative numbers (-3, -1), check to see if their complement (4)
	#   exists in the positive number set
	for i in range(len(n)):
		for j in range(i+1,len(n)):
			target = -1*(n[i]+n[j])
			if target in P:
				res.add(tuple(sorted([n[i],n[j],target])))

	#5. For all pairs of positive numbers (1, 1), check to see if their complement (-2)
	#   exists in the negative number set
	for i in range(len(p)):
		for j in range(i+1,len(p)):
			target = -1*(p[i]+p[j])
			if target in N:
				res.add(tuple(sorted([p[i],p[j],target])))

	return res