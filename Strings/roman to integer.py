def intValue(x):
    if x == "I":
        return 1
    if x == "V":
        return 5
    if x == "X":
        return 10
    if x == "L":
        return 50
    if x == "C":
        return 100
    if x == "D":
        return 500
    if x == "M":
        return 1000
    return -1
    

def romanToInt(A):
    res = 0
    i = 0
    while i < len(A):
        v1 = intValue(A[i])
        if i+1 < len(A):
            v2 = intValue(A[i+1])
            if v1 >= v2:
                res += v1
                i += 1
            else:
                res = res + v2 - v1
                i += 2
        else:
            res += v1
            i += 1

    return res


A = "IIV"
print(romanToInt(A))