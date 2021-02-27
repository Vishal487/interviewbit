def binarySearch(A, B, first):
    n = len(A)
    lo = 0
    hi = n-1
    req_index = -1
    while lo <= hi:
        mid = lo + ((hi - lo)//2)
        if A[mid] == B:
            req_index = mid
            if first:
                hi = mid-1
            else:
                lo = mid+1
        elif A[mid] < B:
            lo = mid+1
        else:
            hi = mid-1
    return req_index
        

def searchRange(A, B):
    return [binarySearch(A, B, True), binarySearch(A, B, False)]
    

A = [5, 17, 100, 111]
B = 3

print(searchRange(A, B))


