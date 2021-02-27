def minimumTotal(A):
    dp = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[i])):
            row.append(0)
        dp.append(row)

    dp[0][0] = A[0][0]
    for i in range(1, len(A)):
        dp[i][0] = A[i][0] + dp[i-1][0]
        dp[i][-1] = A[i][-1] + dp[i-1][-1]

    for i in range(2, len(A)):
        for j in range(1, len(A[i])-1):
            dp[i][j] = A[i][j] + min(dp[i-1][j], dp[i-1][j-1])

    return min(dp[-1])

def anotherDP_sol(A):
    for i in range(len(A)-2, -1, -1):
        for j in range(len(A[i])):
            A[i][j] += min(A[i+1][j], A[i+1][j+1])
    return A[0][0]


A = [
        [2],
        [3,4],
        [6,5,7],
        [4,1,8,3],
        [4,9,7,3,5]
]

print(minimumTotal(A))
print(anotherDP_sol(A))

"""
         [2],
        [3,4],
       [6,5,7],
      [4,1,8,3],
     [4,9,7,3,5]
"""