def equal(A):
    d = dict()
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            s = A[i]+A[j]
            if s in d:
                val = d[s]
                if [i,j] < val:
                    d[s] = [i, j]
            else:
                d[s] = [i, j]
    ans = []
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            s = A[i]+A[j]
            if s in d:
                if len(d[s]) == 2 and d[s][0] < i and d[s][1] != i and d[s][1] != j:
                    val = d[s]
                    d[s].extend([i,j])
                    ans.append(val)
    return sorted(ans)[0]







A = [ 1, 1, 1, 1, 1 ]
print(equal(A))
# if [1,2] != [1,3]:
#     print("hi")
# else:
#     print("bye")