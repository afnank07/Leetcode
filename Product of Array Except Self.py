def productExceptSelf(nums):
    res = [1] * len(nums)
    prefix=1
    postfix=1

    # res = [1, 1, 2, 6]
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]
        print("nums[i]: ", nums[i])
        print("prefix: ", prefix)

    print("res: ", res)

    print("range: ", *range(len(nums)-1, -1, -1))

    for i in range(len(nums)-1, -1, -1):
        res[i] = postfix
        postfix *= nums[i]
        print("nums[i]: ", nums[i])
        print("postfix: ", postfix)

    # # res = [24, 12, 8, 6]
    # for i in range(len(nums)-1, -1, -1):
    #     res[i] *= postfix
    #     postfix *= nums[i]
    #     print("nums[i]: ", nums[i])
    #     print("postfix: ", postfix)

    print("res: ", res)

    return res

nums = [1,2,3,4]
productExceptSelf(nums)