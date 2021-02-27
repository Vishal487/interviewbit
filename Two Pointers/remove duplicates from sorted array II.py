def removeDuplicates(A):
    j = 0
    n = len(A)
    cnt = 0
    for i in range(n-1):
        if A[i] != A[i+1]:
            A[j] = A[i]
            j += 1
            cnt = 1
        elif A[i] == A[i+1] and cnt < 2:
            A[j] = A[i]
            cnt += 1
            j += 1

    A[j] = A[n-1]
    j += 1
    return j


A = [1,2,2, 3]
n = removeDuplicates(A)
for i in range(n):
    print(A[i])
