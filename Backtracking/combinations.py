# def combinations(n, k):
#     lst = [i for i in range(1, n+1)]



def combinationsUtil(A, index, stack, ans, k):
    new = list(stack)
    if len(new) == k:
        ans.append(new)
    for i in range(index, len(A)):
        stack.append(A[i])
        combinationsUtil(A, i+1, stack, ans, k)
        stack.pop()


def combinations(n, k):
    A = [i for i in range(1, n+1)]
    stack = []
    ans = []
    combinationsUtil(A, 0, stack, ans, k)
    return ans


n = 4
k = 2
print(combinations(n, k))





"""
[1,2,3,4,5]
[1,2,3]
"""