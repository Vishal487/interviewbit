def LIS(A):
    n = len(A)
    if n <= 1:
        return n
    dp = [0 for _ in range(n)]
    dp[0] = 1

    overall_max = 0
    for i in range(1, n):
        max_dp_val = 0
        for j in range(i):
            if A[j] < A[i]:
                if max_dp_val < dp[j]:
                    max_dp_val = dp[j]
        dp[i] = max_dp_val + 1
        if overall_max < dp[i]:
            overall_max = dp[i]
    return overall_max

    




A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
print(LIS(A))
