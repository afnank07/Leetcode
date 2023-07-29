# Time complexity: O( log(m) ). The "in" operation on a set is O(1) time complexity. https://wiki.python.org/moin/TimeComplexity
# Space complexity: O(n): cause set basically creates a Hashmap to perform search
# Runtime: Beats 99.10% | Memory: Beats 29.14%

"""
Time complexity of log(m*n) basically means that you continously divide a list in 2, and get rid of any one of them.
Hence figuring that it is a Binary search. 
"""
def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    row_l = 0
    row_r = len(matrix)-1

    while row_l <= row_r:
        row_m = row_l + ((row_r - row_l) // 2)
        if matrix[row_m][0] > target:
            row_r = row_m - 1
        elif matrix[row_m][-1] < target:
            row_l = row_m + 1
        elif target in set(matrix[row_m]):
            return True   
        else:
            return False
    return False 

# ------------------- SECOND APPROACH ----------------- #

# Time complexity: O( n log(m)  ). The "in" operation on a list is O(n) time complexity. https://wiki.python.org/moin/TimeComplexity
# Space complexity: O(1): inplace
# Runtime: Beats 79.23% | Memory: Beats 65.50%

"""
Time complexity of log(n) basically means that you continously divide a list in 2, and get rid of any one of them.
Hence figuring that it is a Binary search. 
"""
def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    row_l = 0
    row_r = len(matrix)-1

    while row_l <= row_r:
        row_m = row_l + ((row_r - row_l) // 2)
        if matrix[row_m][0] > target:
            row_r = row_m - 1
        elif matrix[row_m][-1] < target:
            row_l = row_m + 1
        elif target in matrix[row_m]:
            return True   
        else:
            return False
    return False 

# matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]] ; target = 3
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]] ; target = 13
# matrix = [[1],[3]] ; target = 4
# matrix = [[1],[3],[5]] ; target = 4
# matrix = [[-9],[-6],[-5],[-4]] ; target = -5
# matrix = [[-10,-8],[-6,-5],[-2,-2],[-1,0],[3,4],[7,7],[8,9],[10,10],[11,11],[12,14],[15,16],[17,19],[20,21],[22,22],[25,27],[28,30],[32,32],[35,36]] ; target = 16

print(searchMatrix(matrix, target))