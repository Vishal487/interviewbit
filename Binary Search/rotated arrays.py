def findMin(A):
    n = len(A)
    low = 0
    high = n-1

    while low <= high:
        if A[low] <= A[high]:
            return A[low]
        mid = low + ((high-low)//2)
        next = (mid+1)%n
        prev = (mid-1)%n
        if A[mid] <= A[next] and A[mid] <= A[prev] :
            return A[mid]
        if A[mid] <= A[high]:
            high = mid-1
        elif A[mid] >= A[low]:
            low = mid+1

    


A = [4,5,6,7,0,1,2,3]
print(findMin(A))
