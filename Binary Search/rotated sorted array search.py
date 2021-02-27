def search(A, B):
    n = len(A)
    lo = 0
    hi = n-1

    min_index = 0
    while lo <= hi:
        if A[lo] <= A[hi]:
            min_index = lo
            break
        mid = lo + ((hi - lo)//2)
        next = (mid+1)%n
        prev = (mid-1)%n
        if A[prev] <= A[mid] and A[mid] <= next:
            min_index = mid
            break
        if A[lo] <= A[mid]:
            lo = mid + 1
        elif A[hi] >= A[mid]:
            hi = mid - 1
    
    if A[min_index] == B:
        return min_index

    lo = 0
    hi = min_index-1
    while lo <= hi:
        mid = lo + ((hi - lo)//2)
        if A[mid] == B:
            return mid
        elif A[mid] < B:
            lo = mid + 1
        else:
            hi = mid - 1
    
    lo = min_index + 1
    hi = n-1
    while lo <= hi:
        mid = lo + ((hi - lo)//2)
        if A[mid] == B:
            return mid
        elif A[mid] < B:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

 

A = [4, 5, 6, 7, 0, 1, 2, 3]
B = 10
print(search(A, B))
