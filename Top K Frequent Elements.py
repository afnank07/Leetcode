
def topKFrequent(nums, k):
    holder = {}
    res=[]
    for ele in nums:
        holder[ele] = holder.get(ele, 0)+1
    
    sorted_list  = sorted(holder.items(), key=lambda x:x[1], reverse=True)
    print(holder.items())
    print(sorted_list)

    for i in range(k):
        res.append(sorted_list[i][0])
    
    return res

nums = [1,1,1,2,2,3, 4,4]
k = 2
print(topKFrequent(nums, k))