def findElement(A, B):
    n = len(A)
    lo = 0
    hi = n-1

    peek = 0
    while lo <= hi:
        mid = lo + ((hi-lo)//2)
        if A[mid-1] <= A[mid] and A[mid] >= A[mid+1]:
            peek = mid
            break
        if A[mid-1] <= A[mid] and A[mid] <= A[mid+1]:
            lo = mid
        if A[mid-1] >= A[mid] and A[mid] >= A[mid+1]:
            hi = mid
        
    if A[peek] == B:
        return peek
    
    lo = 0 
    hi = peek
    while lo <= hi:
        mid = lo + ((hi-lo)//2)
        if A[mid] == B:
            return mid
        elif A[mid] < B:
            lo = mid + 1
        else:
            hi = mid - 1
    
    lo = peek
    hi = n-1
    while lo <= hi:
        mid = lo + ((hi-lo)//2)
        if A[mid] == B:
            return mid
        elif A[mid] < B:
            hi = mid - 1
        else:
            lo = mid + 1
    return -1



A = [3, 9, 10, 15, 19, 20, 17, 5, 1]
B = 17

print(findElement(A, B))