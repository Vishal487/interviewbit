
def spiralOrder(A):
    T = 0
    B = len(A) - 1
    L = 0
    R = len(A[0]) - 1
    dir = 0 

    while T<=B and L<=R:
        print("dir: ", dir)
        if dir == 0:
            for i in range(L, R+1):
                print(A[T][i], end=" ")
            print("\n")
            T += 1
            dir = 1
        elif dir == 1:
            for i in range(T, B+1):
                print(A[i][R], end=" ")
            print("\n")
            R -= 1
            dir = 2
        elif dir == 2:
            for i in range(R, L-1, -1):
                print(A[B][i], end=" ")
            print("\n")
            B -= 1
            dir = 3
        elif dir == 3:
            for i in range(B, T-1, -1):
                print(A[i][L], end=" ")
            print("\n")
            L += 1
            dir = 0
   


matrix = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12],
          [13,14,15,16]
        ]

spiralOrder(matrix)