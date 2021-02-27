def solve(A, B):
    n = len(A)
    d = {}
    for i in range(len(A)):
        d[A[i]] = i

    i = 0
    while i < n and B > 0:
        if A[i] != n-i:
            i1 = d[A[i]]
            i2 = d[n-i]

            del d[A[i]]
            del d[n-i]

            A[i1], A[i2] = A[i2], A[i1]

            d[A[i1]] = i1
            d[A[i2]] = i2
            
            B -= 1
        i += 1
    return A



A = [ 8, 2, 7, 4, 5, 6, 3, 1 ]
B = 2
print(solve(A, B))
