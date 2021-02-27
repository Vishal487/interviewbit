def binarySearch(A, B, first):
    n = len(A)
    low = 0
    high = n-1

    reqIndex = -1

    while low <= high:
        mid = low + ((high-low)//2)
        if A[mid] == B:
            reqIndex = mid
            if first:
                high = mid-1
            else:
                low = mid+1
        elif A[mid] < B:
            low = mid+1
        else:
            high = mid-1
    return reqIndex

             


def findCount(A, B):
    firstIndex = binarySearch(A, B, True)
    if firstIndex != -1:
        secondIndex = binarySearch(A, B, False)
        # print(firstIndex, secondIndex)
        return secondIndex-firstIndex+1
    return 0



A = [5, 7, 7, 8, 8, 10]
B = 8
print(findCount(A, B))