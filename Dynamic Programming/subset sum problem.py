def solve(A, target):
    dp = [[False for _ in range(target+1)] for __ in range(len(A))]
    for i in range(len(dp)):
        dp[i][0] = True
    for j in range(len(dp[0])):
        if A[0] == j:
            dp[0][j] = True

    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            if dp[i-1][j]:
                dp[i][j] = True
            else:
                if j >= A[i]:
                    dp[i][j] = dp[i-1][j-A[i]]
    return dp[len(A)-1][target]


A = [3, 34, 4, 12, 5, 2]
B = 30
print(solve(A, B))
