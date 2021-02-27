import math 

def bitCount(A):
    b = bin(A)
    return b.count('1')

def countTotalSetBits(A):
    mod = 1000000007
    count = 0
    i = 1
    while i <= A:
        count += bitCount(i) % mod
        i += 1
    return count % mod

def better_sol(A):
    mod = 1000000007
    count = 0
    n = A+1
    size = int(math.log2(n)) + 1
    po0 = 1
    po1 = 2

    for i in range(size):
        count += (n//po1) * po0
        m = n%po1
        if m > po0:
            count += m - po0
        po0 = po1
        po1 <<= 1
    return count%mod


A = 100
print(countTotalSetBits(A))
print(better_sol(A))