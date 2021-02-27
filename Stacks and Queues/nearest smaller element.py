def prevSmaller(A):
    B = []
    stack = []
    for i in range(len(A)):
        print("B: ", B)
        print("stack: ", stack)
        print("")
        if len(stack) == 0:
            B.append(-1)
        elif len(stack) > 0 and stack[-1] < A[i]:
            B.append(stack[-1])
        elif len(stack) > 0 and stack[-1] >= A[i]:
            while len(stack) > 0 and A[i] <= stack[-1]:
                stack.pop()
            if len(stack) == 0:
                B.append(-1)
            else:
                B.append(stack[-1])
        stack.append(A[i])
    return B



A = [ 34, 35, 27, 42, 5, 28, 39, 20, 28 ]
print(prevSmaller(A))


"""
4 4 2 2 2
"""