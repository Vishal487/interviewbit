def isMatch(A, B):
    n = len(A)
    m = len(B)

    non_start_char = 0
    for e in B:
        if e != '*':
            non_start_char += 1
    if non_start_char > len(A):
        return 0

    dp = [[0 for i in range(m+1)] for j in range(n+1)]

    dp[0][0] = 1

    for j in range(1, m+1):
        if B[j-1] == '*':
            dp[0][j] = dp[0][j-1]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if B[j-1] == '*':
                dp[i][j] = dp[i][j-1] or dp[i-1][j]
            elif B[j-1] == '?' or A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 0

    return dp[n][m]

       


A = 'ab'
B = 'a*??'
print(isMatch(A, B))
