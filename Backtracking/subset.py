

def subsetsUtil(A, index, stack, ans):
    ans.append(list(stack))
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

    


A = [4,1,2]    # unique elements
print(subsets(A))
