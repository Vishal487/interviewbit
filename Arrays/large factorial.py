def fact(A):
    res = 1
    for i in range(1, A+1):
        res = res*i
    return res

print(fact(3))