from bisect import bisect_right as upper_bound 


def findMedian(A):
    row = len(A)
    col = len(A[0])
    mi = A[0][0]
    mx = 0
    for i in range(row):
        if A[i][0] < mi:
            mi = A[i][0]
        if A[i][col-1] > mx:
            mx = A[i][col-1]
    
    required = (row * col + 1) // 2

    while mi < mx:
        mid = mi + ((mx - mi)//2)
        place = [0]

        for i in range(row):
            j = upper_bound(A[i], mid)
            place[0] = place[0] + j
        if place[0] < required:
            mi = mid + 1
        else:
            mx = mid
    return mi





A = [   [5, 17, 100]    ]

print(findMedian(A))

