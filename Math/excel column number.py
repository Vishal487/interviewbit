def titleToNumber(A):
    n = len(A)
    res = 0
    p = 0

    for i in range(n-1, -1, -1):
        d = ord(A[i]) - ord('A') + 1
        res += (d*pow(26, p))
        p += 1

    return res 




A = "AAA"
print(titleToNumber(A))

# AAA -> 703

# AA
# 