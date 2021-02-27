


def findPairForSum(A, target):
    i = 0
    j = len(A) - 1
    
    while i < j:
        if A[i] + A[j] == target:
            return (A[i], A[j])
        elif A[i] + A[j] < target:
            i += 1
        else:
            j -= 1
    return "pair not exist for sum"


def findPairForDiff(A, target):
    i = 0
    j = 1
    A.sort()
    while i < len(A) and j < len(A):
        if i!=j and A[j] - A[i] == target:
            return (A[i], A[j])
        elif A[j] - A[i] < target:
            j += 1
        else:
            i += 1
    return "pait not exist for diff"




A =  [ -259, -825, 459, 825, 221, 870, 626, 934, 205, 783, 850, 398 ]


print(findPairForSum(A, 10))
print(findPairForDiff(A, -42))
