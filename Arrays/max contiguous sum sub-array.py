def maxSubArray(A):
    max_so_far = -99999
    curr_sum = 0
    for i in range(len(A)):
        curr_sum += A[i]
        if curr_sum > max_so_far:
            max_so_far = curr_sum
        if curr_sum < 0:
            curr_sum = 0
    return max_so_far






A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(A))