
def isBST(A):
    stack = []
    root = -999999
    for i in range(len(A)):
        if A[i] < root:
            return 0
        while len(stack) != 0 and A[i] > stack[-1]:
            root = stack.pop()

        if root > A[i]:
            return 0

        stack.append(A[i])
    return 1



A = [7, 7, 10, 10, 9, 5, 2, 8]
print(isBST(A))
