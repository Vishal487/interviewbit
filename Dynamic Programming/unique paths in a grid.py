ans = 0
def uniquePathsWithObstaclesUtil(A, row, col):
    if row >= len(A) or col >= len(A[0]) or A[row][col] == 1:
        return 
    if row == len(A)-1 and col == len(A[0])-1:
        global ans
        ans += 1

    uniquePathsWithObstaclesUtil(A, row, col+1)
    uniquePathsWithObstaclesUtil(A, row+1, col)

def uniquePathsWithObstacles(A):
    if A[0][0] == 1:
        return 0
    uniquePathsWithObstaclesUtil(A, 0, 0)
    global ans
    return ans


def dpSol(A):
    paths = [[0]*len(A[0]) for _ in A]

    if A[0][0] == 0:
        paths[0][0] = 1
    
    for i in range(1, len(A)):
        if A[i][0] == 0:
            paths[i][0] = paths[i-1][0]

    for j in range(1, len(A[0])):
        if A[0][j] == 0:
            paths[0][j] = paths[0][j-1]
    

    for i in range(1, len(A)):
        for j in range(1, len(A[0])):
            if A[i][j] == 0:
                paths[i][j] = paths[i-1][j] + paths[i][j-1]

    return paths[-1][-1]


A = [
  [0,0,0],
  [0,0,0],
  [0,0,0]
]
print(uniquePathsWithObstacles(A))

print(dpSol(A))
