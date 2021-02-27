
def merge(A, B):
    tempA = []
    for e in A:
        tempA.append(e)
    blen = len(B)
    A.extend([0 for _ in range(blen)])
    i = 0
    j = 0
    k = 0
    while i < len(tempA) and j < len(B):
        if tempA[i] <= B[j]:
            A[k] = tempA[i]
            i += 1
            k += 1
        elif tempA[i] > B[j]:
            A[k] = B[j]
            j += 1
            k += 1
    while i < len(tempA):
        A[k] = tempA[i]
        i += 1
        k += 1
    while j < len(B):
        A[k] = B[j]
        j += 1
        k += 1
    


A = [ 1, 2 ]
B = [ -1, 2 ]

merge(A, B)

print(A)