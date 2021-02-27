def maxProfit(A):
    n = len(A)
    if n <= 1:
        return 0
    else:
        arr = [0]*n    # we can make it O(1) space
        curr_min = A[0]
        for i in range(1, n):
            curr_min = min(curr_min, A[i])
            arr[i] = A[i]-curr_min
        # print(arr)
        return max(arr)


A = [1, 4, 5, 2, 4]

print(maxProfit(A))
