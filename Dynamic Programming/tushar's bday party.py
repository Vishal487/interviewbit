def solve(A, B, C):
    max_cap = max(A)
    dp = [999999 for _ in range(max_cap+1)]
    dp[0] = 0
    for i in range(1, max_cap+1):
        for j in range(len(B)):
            cur_cap = B[j]
            cur_cost = C[j]
            if i-cur_cap >= 0 and dp[i] > dp[i-cur_cap]+cur_cost:
                dp[i] = dp[i-cur_cap] + cur_cost
    ans = 0
    for i in range(len(A)):
        ans += dp[A[i]]
    return ans

A = [4,6]  # freinds capacity
B = [1,3]  # dish capacity
C = [5,3]  # cost
print(solve(A, B, C))

