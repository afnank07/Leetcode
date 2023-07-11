def maxArea(height: list[int]) -> int:
    lp=0
    rp=len(height)-1
    stored_area = 0

    while lp<rp:
        width = rp - lp
        if height[lp] < height[rp]:
            ht = height[lp]
            lp += 1
        else:
            ht = height[rp]
            rp -= 1
        area = ht*width

        if area > stored_area:
            stored_area = area

    return stored_area


height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))

# Time: O(n2)

# def maxArea(height: list[int]) -> int:
#     stored_area=0
#     for i in range(len(height)):
#         for j in range(len(height)):
#             width = abs(i-j)
#             length = (lambda:height[j], lambda:height[i])[height[i]<height[j]]() # (lambda:b, lambda:a)[a<b]()
#             area = length*width

#             if area > stored_area:
#                 print("i, j: ", i,j)
#                 print("length*width: ", length, width, length*width)
#                 stored_area = area

#     return stored_area