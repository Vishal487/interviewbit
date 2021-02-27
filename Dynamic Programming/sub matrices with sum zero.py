
def zeroes(A):
    d = dict()
    count = 0
    sum = 0
    for i in range(len(A)):
        sum += A[i]
        if sum == 0:
            count += 1
        if sum in d:
            count += d[sum]
        try:
            d[sum] += 1
        except:
            KeyError
            d[sum] = 1
    return count

def solve(A):
    n = len(A)
    if n == 0:
        return 0
    m = len(A[0])
    if n == 0 and m == 0:
        return 0
    
    ans = 0
    for i in range(m):
        arr = [0]*n
        for j in range(i, m):
            for k in range(n):
                arr[k] += A[k][j]
            print(arr)
            ans += zeroes(arr)
    return ans


A = [[-8, 5, 7],
     [3, 7, -8],
     [5, -8, 9]]

print(solve(A))
