# Time complexity: O(nlogn): cause we are using sort
# Space complexity: O(1): inplace
# Runtime: Beats 49.79% | Memory: Beats 86.36%

def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    nums1[m:] = nums2
    nums1.sort()
    return nums1

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
print(merge(nums1, m, nums2, n))