def mod(x, n, M):
    if n == 0:
        return 1%M 
    if n % 2 == 0:   # even
        p = mod(x, n//2, M)
        return  (p * p) % M
    else:
        p = mod(x, (n-1)//2, M)
        return (x * p * p) % M 


x = 0
n = 1
M = 1

print(mod(x, n, M))
    
