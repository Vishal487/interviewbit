
def isValid(board, x, y, val):
    for j in range(len(board[0])):  # check in row
        if board[x][j] == val:
            return False
    
    for i in range(len(board)):   # check in col
        if board[i][y] == val:
            return False

    smi = (x//3)*3
    smj = (y//3)*3
    for i in range(3):
        for j in range(3):
            if board[smi+i][smj+j] == val:
                return False
    
    return True

def display(board):
    for row in board:
        print(row)
    print("\n")

# def solveSudoku(board, i, j):
#     if i == len(board):
#         display(board)
#         return

#     ni = 0
#     nj = 0
#     if j == len(board[0])-1:
#         ni = i + 1
#         nj = 0
#     else:
#         ni = i
#         nj = j + 1
    
#     if board[i][j] != 0:
#         solveSudoku(board, ni, nj)
#     else:
#         for po in range(1, 10):
#             if isValid(board, i, j, po):
#                 board[i][j] = po
#                 solveSudoku(board, ni, nj)
#                 board[i][j] = 0


# def foo2(board):
#     nb = []
#     for row in board:
#         nr = []
#         for e in row:
#             if e != ".":
#                 nr.append(int(float(e)))
#             else:
#                 nr.append(0)
#         nb.append(nr)
#     for r in nb:
#         print(r)




# def foo(board):
#     nb = []
#     for i in range(len(board)):
#         r = ""
#         for j in range(len(board[0])):
#             r += str(board[i][j])
#         nb.append(list([r]))
#     print(nb)
#     foo2(nb)

#****************

def solveSudokuUtil(board, i, j):
    if i == len(board):
        # display(board)
        print("returning")
        return list(board)

    ni = 0
    nj = 0
    if j == len(board[0])-1:
        ni = i + 1
        nj = 0
    else:
        ni = i
        nj = j + 1
    
    if board[i][j] != 0:
        solveSudokuUtil(board, ni, nj)
    else:
        for po in range(1, 10):
            if isValid(board, i, j, po):
                board[i][j] = po
                solveSudokuUtil(board, ni, nj)
                board[i][j] = 0


def solveSudoku(boardStr):
    board = []
    for row in boardStr:
        nr = []
        for e in row:
            if e != ".":
                nr.append(int(float(e)))
            else:
                nr.append(0)
        board.append(nr)
    
    ansBoard = solveSudokuUtil(board, 0, 0)
    print("ansBoard: ", ansBoard)

    ansBoardStr = []
    for i in range(len(ansBoard)):
        r = ""
        for j in range(len(ansBoard[0])):
            r += str(ansBoard[i][j])
        ansBoardStr.append(list([r]))
    
    for i in range(len(boardStr)):
        boardStr[i] = ansBoardStr[i]
    print(boardStr)



if __name__ == "__main__":
    # board = [
    #             [3, 0, 6, 5, 0, 8, 4, 0, 0],
    #             [5, 2, 0, 0, 0, 0, 0, 0, 0],
    #             [0, 8, 7, 0, 0, 0, 0, 3, 1],
    #             [0, 0, 3, 0, 1, 0, 0, 8, 0],
    #             [9, 0, 0, 8, 6, 3, 0, 0, 5],
    #             [0, 5, 0, 0, 9, 0, 6, 0, 0],
    #             [1, 3, 0, 0, 0, 0, 2, 5, 0],
    #             [0, 0, 0, 0, 0, 0, 0, 7, 4],
    #             [0, 0, 5, 2, 0, 6, 3, 0, 0]
    #                                             ]
    # foo(board)
    # solveSudoku(board, 0, 0)

    board =   [ "53..7....", 
                "6..195...", 
                ".98....6.", 
                "8...6...3", 
                "4..8.3..1", 
                "7...2...6", 
                ".6....28.", 
                "...419..5", 
                "....8..79" ]

    solveSudoku(board)
    # foo2(board)
    