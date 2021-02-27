from collections import defaultdict

def twoSum(A, target):
    d = defaultdict(int)
    for i in range(len(A)):
        if d[target-A[i]]:
            return [d[target-A[i]], i+1]
        if not d[A[i]]:
            d[A[i]] = i+1
        

    return []

A = [ 3, 4]
B = 8
print(twoSum(A, B))
