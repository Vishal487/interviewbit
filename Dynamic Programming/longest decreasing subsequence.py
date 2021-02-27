def LDS(A):
    n = len(A)
    if n <= 1:
        return n
    dp = [0 for _ in range(n)]
    dp[0] = 1
    overall_max = 0
    for i in range(1, n):
        mx = 0
        for j in range(i):
            if A[j] > A[i]:
                if mx < dp[j]:
                    mx = dp[j]
        dp[i] = mx + 1
        if overall_max < dp[i]:
            overall_max = dp[i]
    return overall_max


A = [50, 3, 10, 7, 40, 80]
print(LDS(A))
