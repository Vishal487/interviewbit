import math

def sqrt(A):
    low = 0
    high = A

    if A == 0:
        return 0

    while low < high:
        mid = low + ((high - low)/2) 
        if mid*mid > A:
            high = mid - 1
        else:
            low = mid 
    return int(math.ceil(low))



A = 11
print(sqrt(A))
print(math.floor(math.sqrt(A)))

