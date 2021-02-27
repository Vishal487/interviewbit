def generateMatrix(n):
    A = [[0 for i in range(n)] for j in range(n)]

    val = 1
    T = 0
    B = n-1
    L = 0
    R = n-1
    
    dir = 0

    while L <= R and T <= B:
        # print("dir: ", dir)
        if dir == 0:
            for i in range(L, R+1):
                A[T][i] = val
                val += 1
            T += 1
            dir = 1
        elif dir == 1:
            for i in range(T, B+1):
                A[i][R] = val
                val += 1
            R -= 1
            dir = 2
        elif dir == 2:
            for i in range(R, L-1, -1):
                A[B][i] = val
                val += 1
            B -= 1
            dir = 3
        elif dir == 3:
            for i in range(B, T-1, -1):
                A[i][L] = val
                val += 1
            L += 1
            dir = 0

    return A
        




A = generateMatrix(5)
for e in A:
    print(e)


