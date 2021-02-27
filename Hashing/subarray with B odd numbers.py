def countSubArray(A, B):
    d = dict()
    count = 0
    curr_sum = 0

    for i in range(len(A)):
        if A[i]%2 == 0:
            A[i] = 0
        else:
            A[i] = 1
    
    for i in range(len(A)):
        curr_sum += A[i]
        if curr_sum == B:
            count += 1
        if (curr_sum - B) in d.keys():
            count += d[curr_sum-B]
        try:
            d[curr_sum] += 1
        except:
            KeyError
            d[curr_sum] = 1
    return count


A = [4, 3, 2, 3, 4]
B = 2
print(countSubArray(A, B))

