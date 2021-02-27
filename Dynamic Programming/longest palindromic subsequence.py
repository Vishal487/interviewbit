def LPSUtil(A, B):
    m = len(A)
    dp = [[0 for i in range(m+1)] for j in range(m+1)]

    for i in range(m+1):
        for j in range(m+1):
            if i==0 or j==0:
                dp[i][j] = 0
            elif A[i-1] == B[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][m]

def LPS(A):
    return LPSUtil(A, A[::-1])

A = "fabcxyayx"
print(LPS(A))
