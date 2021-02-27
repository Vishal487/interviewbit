def max_min(A):
    min = A[0]
    max = A[0]
    for i in range(len(A)):
        if A[i] < min:
            min = A[i]
        elif A[i] > max:
            max = A[i]
    return min + max



A = [ 68, 1 ]

print(max_min(A))