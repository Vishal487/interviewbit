def majorityElement(A):
    n = len(A)
    d = dict()
    nby2 = n//2

    for e in A:
        try:
            d[e] += 1
        except:
            KeyError
            d[e] = 1
        if d[e] > nby2:
            return e
    
A = [100]
print(majorityElement(A))
