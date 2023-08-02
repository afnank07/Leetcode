
def mergeSortAlgo(arr:list) -> list:
    low = 0
    high = len(arr) - 1

    def merge(arr, low, mid, high):
        temp = []
        left = low
        right = mid+1
        while left <= mid and right<=high:
            if arr[left] > arr[right]:
                temp.append(arr[right])
                right += 1
            else:
                temp.append(arr[left])
                left+=1

        while left <= mid:
            temp.append(arr[left])
            left += 1

        while right <= high:
            temp.append(arr[right])
            right += 1

        for i in range(low, high+1):
            arr[i] = temp[i-low]
            
        return arr
    
    def mergeSort(arr1, low, high):
        print('arr 1 : ', arr1)
        if low == high: return
        
        mid = int((low+high)/2)
        mergeSort(arr1, low, mid)
        mergeSort(arr1, mid+1, high)
        merge(arr1, low, mid, high)
        print('arr 2 : ', arr1, '\n')
        return 

    mergeSort(arr, low, high)
    return arr

arr = [5, 4, 3, 2, 1 , 8, 6, 2 ,9, 15, 2]
print(mergeSortAlgo(arr))