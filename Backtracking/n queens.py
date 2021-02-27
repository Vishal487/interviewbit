
def isItSafePlace(chess, row, col):
    i = row-1
    j = col
    while i >= 0:
        if chess[i][j] == 1:
            return False
        i -= 1
    
    i = row-1
    j = col-1
    while i >= 0 and j >= 0:
        if chess[i][j] == 1:
            return False
        i -= 1
        j -= 1
    
    i = row-1
    j = col+1
    while i >= 0 and j < len(chess):
        if chess[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True
    


def printQueen(chess, qsf, row, ans):
    if row == len(chess):
        # print(qsf)
        ans.append(list(qsf))
        return

    for col in range(len(chess)):
        if isItSafePlace(chess, row, col):
            chess[row][col] = 1
            s = ""
            for p in range(len(chess)):
                if p == col:
                    s += 'Q'
                else:
                    s += '.'
                
            qsf.append(s)
            printQueen(chess, qsf, row+1, ans)
            qsf.pop()
            chess[row][col] = 0


def nQueen(n):
    chess = [[0 for i in range(n)] for j in range(n)]
    ans = []
    printQueen(chess, [], 0, ans)
    print("ans: \n", ans)
    return ans



if __name__ == "__main__":
    n = 4
    print(nQueen(n))


"""
0-1,1-3,2-0,3-2,
0-2,1-0,2-3,3-1,
"""