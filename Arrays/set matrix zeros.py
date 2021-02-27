def setZeroes(A):
    nr = len(A)
    nc = len(A[0])

    row = []
    col = []

    for i in range(nr):
        if sum(A[i]) < nc:
            row.append(i)
    
    for j in range(nc):
        cc = [item[j] for item in A]
        # print("cc : ", cc)
        if sum(cc) < nr:
            col.append(j)

    for i in row:
        for j in range(nc):
            A[i][j] = 0
    
    for j in col:
        for i in range(nr):
            A[i][j] = 0
 
    # print("row: ", row)
    # print("col: ", col)

    return A


def setZeroes_sol2(A):
    """
        here we take care of 1st row and col using two flags
        and then uses 1st row and col as a extra space used in previous 
        method (`row` and `col`) for remaining part of matrix.
    """
    rowFlag = 0
    colFlag = 0
    for i in range(len(A)):
        if A[i][0] == 0:
            colFlag = 1
            break
    for i in range(len(A[0])):
        if A[0][i] == 0:
            rowFlag = 1
            break

    for i in range(1, len(A)):
        for j in range(1, len(A[0])):
            if A[i][j] == 0:
                A[i][0] = 0
                A[0][j] = 0
    
    for i in range(1, len(A)):
        for j in range(1, len(A[0])):
            if A[i][0] == 0 or A[0][j] == 0:
                A[i][j] = 0

    if rowFlag == 1:
        for i in range(len(A[0])):
            A[0][i] = 0

    if colFlag == 1:
        for i in range(len(A)):
            A[i][0] = 0

    return A



A = [   [1, 0, 1],
        [1, 1, 1], 
        [1, 1, 1]   ]

A = setZeroes_sol2(A)
for e in A:
    print(e)
