def reverse(A):
    numl = ['0' for i in range(32)]
    ind = 31
    while A > 0:   # O(log A)
        numl[ind] = str(A%2)
        ind -= 1
        A = A//2
    num = "".join(numl)  
    # rev = num[::-1]
    # no need to take reverse bcz
    # to find corresponding decimal
    # we have to traverse from left side of 
    # binary representation

    # print("num, rev : ", num, rev)
    ans = 0
    p = 0
    for b in num:
        b = int(float(b))
        ans += (b*pow(2, p))
        p += 1

    return ans
    



A = 3
print(reverse(A))