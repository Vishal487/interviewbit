def countPairs(A, B):
    cnt = 0
    d = dict()
    for e in A:
        d[e] = 1
    for i in range(len(A)):
        a = A[i]
        b = a ^ B
        if b in d:
            cnt += 1
    return cnt//2   # bcz we count all duplicates






A = [3, 6, 8, 10, 15, 50]
B = 5
print(countPairs(A, B))
