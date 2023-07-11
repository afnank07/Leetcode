def twoSum(numbers: list[int], target: int) -> list[int]:
    lp=0
    rp=len(numbers)-1
    while lp<rp:
        if numbers[lp]+numbers[rp]>target:
            rp-=1
            print("if: ", lp, rp, numbers[lp],numbers[rp])
            continue

        print("out if: ", lp, rp, numbers[lp],numbers[rp])
        if numbers[lp]+numbers[rp] == target:
            return [lp+1, rp+1]
        # elif numbers[lp]+numbers[rp] > target:
        #     lp+=1
        
        lp+=1
        # rp-=1





numbers = [2,7,11,15]
target = 9

# numbers = [2,3,4]
# target = 6

# numbers = [-1,0]
# target = -1

numbers = [5,25,75]
target = 100
print(twoSum(numbers, target))