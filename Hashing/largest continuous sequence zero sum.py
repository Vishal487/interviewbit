def solve(A):
    sumArray = []
    d = dict()
    d[0] = -1
    s = 0
    st = end = 0
    for i in range(len(A)):
        s += A[i]
        if s in d.keys():
            if (i - d[s]) > (end-st):
                st = d[s]
                end = i
        else:
            d[s] = i
    return A[st+1:end+1]


A = [1, 2, -3, 3]
print(solve(A))
