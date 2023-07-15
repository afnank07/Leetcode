# Time complexity O(n2): cause we are looping through every ele just once 
# Memory 
# Runtime: Beats 8.36% | Memory: Beats 59.02%
def setZeroes(matrix: list[list[int]]) -> None:
    rows = []
    cols = []
    for i, lst in enumerate(matrix):
        if 0 in lst:
            for j, ele in enumerate(lst):
                if ele == 0: 
                    rows.append(i)
                    cols.append(j)

    for i, lst in enumerate(matrix):
        if i in rows:
            matrix[i] = list(map(lambda x,y : x*y, lst, [0]*len(lst)))
        for j, ele in enumerate(lst):
            if j in cols:
                matrix[i][j] = 0
    
    
    return matrix

matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(setZeroes(matrix))