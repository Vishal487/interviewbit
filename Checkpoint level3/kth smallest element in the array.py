def kthSmallest(A, k):   # A is read-only
    temp = sorted(A)     # space : O(len(A))
    return temp[k-1]


def binarySearch_Sol(A, B):
    n = len(A)
    low = 0
    high = max(A)    # O(n)
    res = 0

    while low <= high:
        mid = low + ((high-low)//2)
        lt_count = 0
        gt_count = 0
        eq_count = 0
        for e in A:
            if e < mid:
                lt_count += 1
            elif e > mid:
                gt_count += 1
            else:
                eq_count += 1
        if lt_count < B:
            if lt_count + eq_count >= B:
                low = mid
                break
            low = mid + 1
        else:
            high = mid - 1
    
    for e in A:
        if e <= low:
            res = max(res, e)
    return res


    



A = [ 8, 16, 80, 55, 32, 8, 38, 40, 65, 18, 15, 45, 50, 38, 54, 52, 23, 74, 81, 42, 28, 16, 66, 35, 91, 36, 44, 9, 85, 58, 59, 49, 75, 20, 87, 60, 17, 11, 39, 62, 20, 17, 46, 26, 81, 92 ]
k = 9
print(kthSmallest(A, k))
print(binarySearch_Sol(A, k))