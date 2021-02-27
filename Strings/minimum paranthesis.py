def solve(A):   # time O(len(A)) and space : O(len(A)) in worst case
    stack = []
    for i in range(len(A)):
        if A[i] == ')' and len(stack) != 0 and stack[-1] == '(':
            stack.pop()
        else:
            stack.append(A[i])
    return len(stack)

def sol2(A):   # time O(len(A)) and space : O(1)
    cnt_open = 0
    cnt_close = 0
    for e in A:
        if e == "(":
            cnt_open += 1
        else:
            cnt_close += 1
    return abs(cnt_open - cnt_close)

A = '(()('
print(solve(A))
print(sol2(A))
