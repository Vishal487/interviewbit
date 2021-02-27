def minPathSum(A):
    dp = [[0 for j in range(len(A[0]))] for i in range(len(A))]

    dp[0][0] = A[0][0]

    for i in range(1, len(A)):
        dp[i][0] = A[i][0] + dp[i-1][0]
    for j in range(1, len(A[0])):
        dp[0][j] = A[0][j] + dp[0][j-1]

    for i in range(1, len(A)):
        for j in range(1, len(A[0])):
            dp[i][j] = A[i][j] + min(dp[i-1][j], dp[i][j-1])

    return dp[-1][-1]

A = [  [1, 3, 2],
        [4, 3, 1],
        [5, 6, 1]
     ]

print(minPathSum(A))
