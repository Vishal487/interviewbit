def braces(A):
    stack = []
    operators = ['+', '-', '*', '/']
    for e in A:
        if e == "(" or e in operators :
            stack.append(e)
        elif e == ")":
            popped1 = stack.pop()
            if popped1 in operators:
                stack.pop()
            else:
                return 1
    return 0




A = "(a)"
print(braces(A))


"""
((a+b) + (c+d))

"""