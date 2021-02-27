

def subsetsUtil(A, index, stack, ans):
    new = list(stack)
    if new not in ans:
        ans.append(new)
    for i in range(index, len(A)):
        stack.append(A[i])
        subsetsUtil(A, i+1, stack, ans)
        stack.pop()


def subsets(A):
    A.sort()
    stack = []
    ans = []
    subsetsUtil(A, 0, stack, ans)
    return ans

    


A = [4,2,2]
print(subsets(A))
