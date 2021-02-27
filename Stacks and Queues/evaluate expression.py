def evalRPN(A):
    stack = []
    operations = ['+', '-', '*', '/']
    for e in A:
        if e in operations:
            op2 = stack.pop()
            op1 = stack.pop()
            if e == "+":
                res = op1 + op2
            elif e == "-":
                res = op1 - op2
            elif e == "*":
                res = op1 * op2
            else:
                res = op1 // op2 
            stack.append(res)
        else:
            stack.append(int(float(e)))
    return stack[-1]






A =   ["4", "13", "5", "/", "+"]
print(evalRPN(A))
