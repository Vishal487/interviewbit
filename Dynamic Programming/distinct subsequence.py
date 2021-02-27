def numDistinct(A, B):   # find B in A, S in T
    m = len(A)    # bigger
    n = len(B)

    if m < n:
        return 0

    dp = [[0 for j in range(m+1)] for i in range(n+1)]

    for i in range(1, n+1):
        dp[i][0] = 0
    for j in range(m+1):
        dp[0][j] = 1
    # print("done")
    for i in range(1, n+1):
        for j in range(1, m+1):
            if A[j-1] != B[i-1]:
                dp[i][j] = dp[i][j-1]
            else:
                dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
    return dp[n][m]



A = "rabbbit"
B = "rabbit"
print(numDistinct(A, B))
