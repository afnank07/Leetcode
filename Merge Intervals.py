# Time complexity: O(nlogn) + O(n): cause we are using sort and a loop
# Space complexity: O(1): inplace
# Runtime: Beats 61.41% | Memory: Beats 94.34%

def merge(intervals: list[list[int]]) -> list[list[int]]: 
    if len(intervals) == 1:
        return intervals
    
    intervals.sort()
    lp=0
    rp=1

    while rp < len(intervals):
        # does lp overlap with rp
        if ( (intervals[lp][1] >= intervals[rp][0]) and (intervals[lp][1] <= intervals[rp][1]) ):
            intervals[lp][1] = intervals[rp][1]

        # does lp overlap with rp and rp is subset of lp
        elif ( (intervals[lp][1] >= intervals[rp][0]) and (intervals[lp][1] > intervals[rp][1]) ):
            rp+=1
            continue

        # lp does not overlap with rp
        else:
            lp += 1
            intervals[lp] = intervals[rp]
            
        rp+=1

    return intervals[:lp+1]

# intervals = [[1,3],[2,6],[8,10],[15,18]]
# intervals = [[1,4],[4,5]] # (intervals[lp][1] >= intervals[rp][0]): = sign added
# intervals = [[1,4],[1,4]] # (intervals[lp][1] <= intervals[rp][1]): = sign added
intervals = [[1,4],[2,3]]

print(merge(intervals))

# ------------------- OTHER APPROACH ----------------- #

# Time complexity: O(nlogn) + O(n): cause we are using sort and a loop
# Space complexity: O(n): cause we are using a list to store intervals 
# Runtime: Beats 52.65% | Memory: Beats 55.36%
def merge_1(intervals: list[list[int]]) -> list[list[int]]:
    res=[]    
    intervals.sort()

    lp=0
    rp=1

    while rp < len(intervals):
        if ( (intervals[lp][1] >= intervals[rp][0]) and (intervals[lp][1] <= intervals[rp][1]) ):
            intervals[lp][1] = intervals[rp][1]
        elif ( (intervals[lp][1] >= intervals[rp][0]) and (intervals[lp][1] > intervals[rp][1]) ):
            rp+=1
            continue
        else:
            res.append(intervals[lp])
            lp = rp
        rp+=1

    res.append(intervals[lp])
    return res

# intervals = [[1,3],[2,6],[8,10],[15,18]]
# intervals = [[1,4],[4,5]] # (intervals[lp][1] >= intervals[rp][0]): = sign added
# intervals = [[1,4],[1,4]] # (intervals[lp][1] <= intervals[rp][1]): = sign added
# intervals = [[1,4],[2,3]]

# print(merge(intervals))