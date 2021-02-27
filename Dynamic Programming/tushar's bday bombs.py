def solve(A, B):
    n = len(B)
    minn = min(B)

    hits = A//minn
    ans = []
    i = 0
    while A >= 0:
        if A-B[i] >= (hits-1)*minn:
            A -= B[i]
            hits -= 1
            ans.append(i)
        else:
            i += 1
    ans.pop()
    return ans


A = 11
B = [6, 8, 4, 2, 7]
print(solve(A, B))