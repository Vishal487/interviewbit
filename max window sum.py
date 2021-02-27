
def maxWindowSum(A, k):     # k:window size
    i = 0
    j = k-1
    ii = i
    jj = j
    curr_sum = sum(A[i:k]) 
    max_sum = curr_sum
    while j < len(A)-1:
        j += 1
        curr_sum = curr_sum + A[j] - A[i]
        i += 1
        if curr_sum > max_sum:
            max_sum = curr_sum
            ii = i
            jj = j
    return (ii, jj, max_sum)


A = [5,18,1,6,4,9,7]

print(maxWindowSum(A, 5))