def singleNumber(A):
    d = dict()
    for e in A:
        try:
            d[e] += 1
        except:
            KeyError
            d[e] = 1
    for k,v in d.items():
        if v == 1:
            return k





A = [1, 2, 4, 3, 3, 2, 2, 3, 1, 1]
print(singleNumber(A))
