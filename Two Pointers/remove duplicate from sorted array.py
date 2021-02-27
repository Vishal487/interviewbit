def removeDuplicates(A):
    n = len(A)
    j = 0
    for i in range(n - 1):
        if A[i] != A[i+1]:
            A[j] = A[i]
            j += 1
    A[j] = A[n-1]
    j += 1
    return j
    




A = [1, 1, 2, 2, 3]
j = removeDuplicates(A)
print("j: ", j)
for i in range(j):
    print(A[i])
