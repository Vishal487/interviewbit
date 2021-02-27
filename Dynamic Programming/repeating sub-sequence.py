
def LRS(A):
    m = len(A)
    B = str(A)
    dp = [[0 for j in range(m+1)] for i in range(m+1)]

    for i in range(m+1):
        for j in range(m+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif A[i-1] == B[j-1] and i-1 != j-1:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # return dp[m][m]   # it returns length
    return (1 if dp[m][m] >= 2 else 0)

A = "aaa"
print(LRS(A))
