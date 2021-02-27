def isScramble(A, B):
    if len(A) != len(B):
        return 0
    if len(A) == 0:   # both strings are empty => scramble
        return 1
    if A == B:  
        return 1
    if sorted(A) != sorted(B):  # anagram
        return 0
    # now main part
    n = len(A)
    for i in range(1, n):
        if isScramble(A[:i], B[:i]) and isScramble(A[i:], B[i:]):
            return 1
        if isScramble(A[-i:], B[:i]) and isScramble(A[:-i], B[i:]):
            return 1
    
    return 0


A = "great"
B = "rgeat"
print(isScramble(A, B))
