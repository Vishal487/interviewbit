def findMedianSortedArray(A, B):
    n = len(A)
    m = len(B)
    temp = [0 for i in range(n+m)]
    i = 0
    j = 0
    k = 0
    l = n+m
    while i < n and j < m and k <= (l//2):
        if A[i] < B[j]:
            temp[k] = A[i]
            i += 1
            k += 1
        else:
            temp[k] = B[j]
            j += 1
            k += 1
    while i < n:
        temp[k] = A[i]
        i += 1
        k += 1
    while j < m:
        temp[k] = B[j]
        j += 1
        k += 1
    # print(temp)
    # l = n+m
    # print(l)
    if l%2 == 0:  # even
        med = (temp[(l//2)-1] + temp[l//2])/2.0
    else:
        med = temp[l//2]
    return med


A = [1,4]
B = [2,3]

print(findMedianSortedArray(A, B))