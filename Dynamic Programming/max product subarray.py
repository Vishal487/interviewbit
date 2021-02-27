def maxProduct(A):
    n = len(A)
    if n == 0:
        return 0
    if n == 1:
        return A[0]
    max_ending_here = min_ending_here = max_overall = A[0]
    for i in range(1, n):
        temp = max_ending_here
        max_ending_here = max(A[i], max_ending_here*A[i], min_ending_here*A[i])
        min_ending_here = min(A[i], min_ending_here*A[i], temp*A[i])
        max_overall = max(max_overall, max_ending_here)
    return max_overall


A = [2, 3, -2, 4, -5, 2, -6, 1, 2, 5, 9]
print(maxProduct(A))
