def removeElement(A, B):
    left = 0

    for i in range(len(A)):
        if A[i] != B:
            A[left] = A[i]
            left += 1
    return left







A = [4, 1, 1, 2, 1, 3]
B = 1

n = removeElement(A, B)
print(n)
for i in range(n):
    print(A[i])