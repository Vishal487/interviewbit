def maxOne(A, B):
    max_one = 0
    left = 0
    zero_cnt = 0
    si = 0
    li = 0
    for i in range(len(A)):
        if A[i] == 0:
            zero_cnt += 1
        
        while zero_cnt > B:
            if A[left] == 0:
                zero_cnt -= 1
            left += 1

        curr_max = i - left + 1
        if curr_max > max_one:
            max_one = curr_max
            si = left
            li = i
    return [i for i in range(si, li+1)]

        




A = [1, 1, 0, 1, 1, 0, 0, 1, 1, 1]
B = 2

print(maxOne(A, B))