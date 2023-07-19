"""
This problem has a algorithm. 

Step1: Traverse the array backwards until the numbers start decreasing 
Step2: Swap the first decreasing number with the consecutive larger number from the traversed array in step1
Step3: Reverse the traversed array 
"""
def nextPermutation(nums: list[int]) -> None:
    # edge case: when nums=[1,1] -> idx will not be initialised hence declare it 
    idx=-1
    # Step1
    for i in range(len(nums)-1, -1, -1):
        if nums[i] > nums[i-1]:
            idx = i-1
            break
    
    # if lexicographical order is not possible then just sort the list 
    if idx == -1:
        nums.sort()
    else:
        # Step2
        for i in range(len(nums)-1, -1, -1):
            if nums[i] > nums[idx]:
                temp = nums[idx]
                nums[idx] = nums[i]
                nums[i] = temp
                break
        
        # Step3
        nums[idx+1:] = nums[idx+1:][::-1]
    return nums

nums = [1,1]
print(nextPermutation(nums))