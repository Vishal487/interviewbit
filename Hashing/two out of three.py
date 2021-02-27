def solve(A, B, C):
    d = dict()
    A = set(A)
    B = set(B)
    C = set(C)

    for e in A:
        try:
            d[e] += 1
        except:
            KeyError
            d[e] = 1
    for e in B:
        try:
            d[e] += 1
        except:
            KeyError
            d[e] = 1
    for e in C:
        try:
            d[e] += 1
        except:
            KeyError
            d[e] = 1
    ans = []
    for k,v in d.items():
        if v >= 2:
            ans.append(k)
    ans.sort()
    return ans

           

A = [1, 2]
B = [1, 3]
C = [2, 3]
print(solve(A, B, C))
