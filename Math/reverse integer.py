def reverse(A):
    isNeg = False
    if A < 0:
        A = -A
        isNeg = True
    
    n = 0
    while A >= 10:
        digit = A%10
        n = (n*10) + digit
        A = A//10
    n = (n*10) + A
    if n < -2147483648  or n > 2147483647:
        return 0
    if isNeg:
        return -n
    return n


A = -1146467
print(reverse(A))