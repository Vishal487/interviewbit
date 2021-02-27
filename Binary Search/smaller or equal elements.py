def solve(A, B):
    n = len(A)
    lo = 0
    hi = n-1
    req_index = -1
    while lo <= hi:
        mid = lo + ((hi-lo)//2)
        if A[mid] <= B: 
            req_index = mid
            lo = mid + 1
        elif A[mid] > B:
            hi = mid-1
    return req_index+1






A = [1, 2, 5, 5]
B = 0
print(solve(A, B))
