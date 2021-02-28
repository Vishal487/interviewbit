def median(A):
    A.sort()
    n = len(A)
    if n%2 != 0:    # odd
        return A[n//2]
    else:
        return (A[n//2] + A[(n//2)-1])//2

def seats(A):
    arr = []
    sub = 0
    for i in range(len(A)):
        if A[i] == 'x':
            arr.append(i-sub)
            sub += 1
    if len(arr) <= 1:
        return 0
    MOD = 10000003
    med = median(arr)
    ans = 0
    for e in arr:
        ans += abs(med - e)%MOD
    return int(ans)%MOD



A = "...xx..x.xx"
print(seats(A))
