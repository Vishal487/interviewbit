def commonPrefixOfTwoString(A, B):
    i = 0
    while i<len(A) and i<len(B):
        if A[i] != B[i]:
            break
        i += 1
    return A[:i]

def longestCommonPrefix(A):
    # no need to sort :)
    prefix = A[0]
    for i in range(1, len(A)):
        if prefix not in A[i]:
            prefix = commonPrefixOfTwoString(prefix, A[i])
            
    return prefix
    




A = ["abcdefgh", "aefghijk", "abcefgh"]
# A = ["abab", "ab", "abcd"]
print(longestCommonPrefix(A))
