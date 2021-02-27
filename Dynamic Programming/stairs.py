def climbStairsUtil(A, dp):
    if A == 0:
        return 1
    if A < 0:
        return 0
    if dp[A] != 0:
        return dp[A]

    cnt1 = climbStairsUtil(A-1, dp)
    cnt2 = climbStairsUtil(A-2, dp)
    dp[A] = cnt1 + cnt2
    return dp[A]

def climbStairs_Memo(A):
    dp = [0 for _ in range(A+1)]
    dp[0] = 1
    climbStairsUtil(A, dp)
    print(dp)
    return dp[A]

def climbStairs(n):
    dp = [0 for _ in range(n+1)]
    dp[0] = 1
    for i in range(1, n+1):
        if i == 1:
            dp[i] = dp[i-1]
        else:
            dp[i] = dp[i-1] + dp[i-2]
    print(dp)
    return dp[n]



A = 2
print("memoization method")
print(climbStairs_Memo(A))
print("tabulation method")
print(climbStairs(A))