def distinct_count(A):
    if len(A) == 0:
        return 0
    cnt = 1
    A.sort()
    for i in range(len(A)-1):
        if A[i] != A[i+1]:
            cnt += 1
    # print(cnt)
    return cnt

def dNums(A, B):
    n = len(A)
    if B == 1:
        return [1]*n
    if B > n:
        return []
    dic = {}
    # dic will always hold values such that their counts sum up to B
    res = []
    for i in range(n):
        if A[i] not in dic:
            dic[A[i]] = 1
        else:
            dic[A[i]] += 1
        # after the first window we start to remove from dict
        if i >= B:
            if dic[A[i - B]] == 1:
                del dic[A[i - B]]
            else: 
                dic[A[i - B]] -= 1
        # after the first window we start to append to result
        if i + 1 >= B:
            res.append(len(dic))
    return res
            


A = [ 80, 18, 80, 80, 80, 80, 80, 80, 94, 18 ]
B = 8
print(dNums(A, B))
# distinct_count(A)
