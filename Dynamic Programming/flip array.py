def solve(A):
    ts = sum(A)
    hs = ts//2

    dp = [99999 for _ in range(hs+1)]
    dp[0] = 0
    for i in range(len(A)):
        for j in range(hs, A[i]+1, -1):
            if dp[j-A[i]] != 99999 :
                dp[j] = min(dp[j], dp[j-A[i]]+1)
    print(dp)
    for i in range(hs, -1, -1):
        if dp[i] != 99999:
            return dp[i]

A = [5,4,1]
print(solve(A))
