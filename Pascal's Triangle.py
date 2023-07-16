# Time complexity O(n2): cause we are looping through every ele just once 
# Memory O(n2)
# Runtime: Beats 81.71% | Memory: Beats 78.52%

# NOTE: You can get the each element by it's row and column using nCr formula
# Link: https://takeuforward.org/data-structure/program-to-generate-pascals-triangle/

def generate(numRows: int) -> list[list[int]]:
    ans = [[1]]

    for r in range(numRows-1):
        temp = [0] + ans[-1] + [0]
        res =[]
        for c in range(len(ans[-1])+1):
            res.append(temp[c] + temp[c+1])

        ans.append(res)
    return ans

numRows = 5
print(generate(numRows))

# ------------------- OTHER APPROACHES ----------------- #

# Time complexity O(n2): cause we are looping through every ele just once 
# Memory O(n2)
# Runtime: Beats 34.35% | Memory: Beats 7.71%
def generate_1(numRows: int) -> list[list[int]]:
    ans = [[1], [1, 1]]
    if numRows==1:
        return [ans[0]]
    elif numRows==2:
        return ans
    
    for i in range(2, numRows):
        res=[1]
        for j in range(1, i):
            res.append(ans[i-1][j-1] + ans[i-1][j])
        res.append(1)
        ans.append(res.copy())
    
    return ans

# numRows = 5
# print(generate(numRows))