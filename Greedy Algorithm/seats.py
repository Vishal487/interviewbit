def median(A):
    A.sort()
    n = len(A)
    if n%2 != 0:    # odd
        return A[n//2]
    else:
        return (A[n//2] + A[(n//2)-1])//2

def seats(A):
    arr = []
    sub = 0
    for i in range(len(A)):
        if A[i] == 'x':
            arr.append(i-sub)
            sub += 1
    if len(arr) <= 1:
        return 0
    MOD = 10000003
    med = median(arr)
    ans = 0
    for e in arr:
        ans += abs(med - e)%MOD
    return int(ans)%MOD


# with better understanding 
def sol2(A):
    index_arr = []
    for i in range(len(A)):
        if A[i] == 'x':
            index_arr.append(i)
    if len(index_arr) <= 1:
        return 0
    MOD = 10000003
    mid = len(index_arr)//2
    center_pos = index_arr[mid]
    ans = 0
    for i in range(len(index_arr)):
        start_ind = index_arr[i]
        end_ind = center_pos - mid + i
        ans += abs(start_ind - end_ind)%MOD
    return ans%MOD


A = "...xx.."
print(seats(A))
print(sol2(A))
