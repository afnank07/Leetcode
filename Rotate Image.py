# Time complexity O(n2)
# Space complexity: O(1)
# Runtime: Beats 54.18% | Memory: Beats 87.76%

"""
Intuition: Figuring out that, there is a transpose of matrix required and then reversing each row 
"""
def rotate(matrix: list[list[int]]) -> None:

    # Transpose a matrix 
    for i in range(0,len(matrix)-1):
        for j in range(i+1, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]  # swap

    # Reverse every row
    for i in range(len(matrix)):
        matrix[i] = matrix[i][::-1]
        
    return matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate(matrix))