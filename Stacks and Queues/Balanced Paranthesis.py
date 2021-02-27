def isBalanced(A):
    stack = []
    for e in A:
        if e =="(":
            stack.append(e)
        elif e == ")":
            try:
                stack.pop()
            except:
                IndexError
                return 0
    return int(len(stack) == 0)
    


A = "()"
print(isBalanced(A))