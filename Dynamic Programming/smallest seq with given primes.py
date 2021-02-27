def uglyNumber(A, B, C, D):
    dp = [1]
    i,j,k = 0,0,0
    for _ in range(D):
        curr = (min(A*dp[i], B*dp[j], C*dp[k]))
        if curr == A*dp[i]:
            i += 1
        if curr == B*dp[j]:
            j += 1
        if curr == C*dp[k]:
            k += 1
        dp.append(curr)
    return dp[1:]

A = 2
B = 3
C = 5
D = 5
print(uglyNumber(A, B, C, D))


