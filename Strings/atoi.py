def atoi(A):
    MAX_INT = 2**31 - 1
    MIN_INT = -2**31

    A = A.strip()

    negFlag = 1
    if A[0] == "-":
        negFlag = -1
    
    i = 0
    j = len(A)
    if A[0] == "+" or A[0] == "-":
        i += 1
    
    res = 0
    while i < j:
        if '0' <= A[i] <= '9':
            res = res*10 + (ord(A[i]) - 48)
        else:
            break
        i += 1

    res = res*negFlag

    return max(MIN_INT, min(MAX_INT, res))


        


A = "5121478262 8070067M75"
print(atoi(A))
