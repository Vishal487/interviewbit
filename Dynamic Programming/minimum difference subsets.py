def findSubsetSum(A, target):
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
    return dp[-1]


def solve(A):
    total_sum = sum(A)
    half_sum = total_sum//2
    dp = findSubsetSum(A, half_sum)
    for i in range(len(dp)-1, -1, -1):
        if dp[i] == True:
            break
    return abs((total_sum - i) - i)

A = [1, 6, 11, 5]
print(solve(A))
