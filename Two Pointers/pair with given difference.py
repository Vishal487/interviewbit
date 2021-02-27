# unsorted
# [1, 2, 3, 4]

def findPair(A, B):
    A.sort()
    i = 0
    j = 1

    while j<len(A) and i <= len(A):
        if i!=j and (A[j]-A[i]) == B:
            return 1
        elif (A[j]-A[i]) < B:
            j += 1
        else:
            i += 1
    return 0


A = [ -259, -825, 459, 825, 221, 870, 626, 934, 205, 783, 850, 398 ]

B = -42
print(findPair(A, B))
