from collections import defaultdict

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

def isValidSudoku(board):
    rows = defaultdict(list)
    cols = defaultdict(list)
    square = defaultdict(list)

    for r in range(9):
        for c in range(9):

            if board[r][c] == ".":
                continue

            if board[r][c] in rows[r] and board[r][c] in cols[c] and board[r][c] in square[(r//3,c//3)]:
                return False
            
            rows[r].append(board[r][c])
            cols[c].append(board[r][c])
            square[(r//3,c//3)].append(board[r][c])

            print("rows: ", r)
            print("cols: ", c)
            print("square: ", r//3, c//3)
    
    return True

res = isValidSudoku(board)
print(res)