def solve(val, wt, W):
    n = len(val)
    
    dp = [[0 for _ in range(W+1)] for __ in range(n+1)]

    for i in range(n+1):
        for w in range(W+1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif wt[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], val[i-1]+dp[i-1][w-wt[i-1]])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][W]

A = [60, 100, 120]
B = [10, 20, 30]
C = 50

print(solve(A, B, C))
