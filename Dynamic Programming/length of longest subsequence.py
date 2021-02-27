

def longestSubsequenceLength(A):
    n = len(A)
    if n == 0:
        return 0
    LIS = [1 for i in range(n)]
    LDS = [1 for i in range(n)]

    for i in range(1, n):
        for j in range(i):
            if A[i] > A[j] and LIS[i] <= LIS[j]+1:
                LIS[i] = LIS[j] + 1
    
    for i in range(n-2, -1, -1):
        for j in range(n-1, i, -1):
            if A[i] > A[j] and LDS[i] <= LDS[j]:
                LDS[i] = LDS[j] + 1

    ans = LIS[0] + LDS[0] - 1
    for i in range(1, n):
        ans = max(ans, LIS[i]+LDS[i]-1)
    return ans




A = [1, 2, 1]
print(longestSubsequenceLength(A))
