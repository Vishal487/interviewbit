def gcd_rec(A, B):
    if A == 0:
        return B
    if B == 0:
        return A

    # base case
    if A == B:
        return A
    if A < B:
        return gcd(A, B-A)
    return gcd(A-B, B)


def gcd(A, B):
    if A == 0:
        return B
    if B == 0:
        return A

    if A == B:
        return A

    while A != B:
        if A < B:
            B = B-A
        elif A > B:
            A = A - B

    return A




A = 6
B = 9

print(gcd(A, B))