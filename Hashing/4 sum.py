def fourSum(A, target):
    A.sort()
    result = set()

    for i in range(len(A)):
        for j in range(i+1, len(A)):
            lo = j+1
            hi = len(A)-1
            while lo < hi:
                x = A[i] + A[j] + A[lo] + A[hi]
                if x == target:
                    result.add((A[i], A[j], A[lo], A[hi]))
                    lo += 1
                    hi -= 1
                elif x < target:
                    lo += 1
                else:
                    hi -= 1
    return sorted(result)


A = [1,0,-1,0,-2,2]
B = 0
print(fourSum(A, B))
