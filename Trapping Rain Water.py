def trap(height: list[int]) -> int:
    lp=0
    rp = len(height)-1
    maxL = height[lp]
    maxR = height[rp]
    totalWaterUnit=0

    while lp<rp:
        if height[lp] < height[rp]:
            waterUnit = max((maxL - height[lp]),0)
            maxL = max(maxL, height[lp])
            lp+=1 
        else:
            waterUnit = max((maxR - height[rp]),0)
            maxR = max(maxR, height[rp])
            rp-=1
        
        # print("before: ", waterUnit)
        # print("before: ", waterUnit)
        totalWaterUnit += waterUnit
        # print("after: ",totalWaterUnit)

    return totalWaterUnit


height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))