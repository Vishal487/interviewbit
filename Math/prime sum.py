import math

def isPrime(A):
    if A < 2:
        return False
    i = 2
    while i < int(math.sqrt(A))+1:
        if A%i == 0:
            return False
            break
        i += 1
    else:
        return True


def primeSum(A):
    # allPrimes = dict()
    i = 2
    while i < A:
        if isPrime(i) and isPrime(A-i):
            return [i, A-i]
        i += 1
        

    

A = 16777214
ans = primeSum(A)
print(ans)