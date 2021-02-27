def maxOnes(A, B):
    left = 0
    zero_count = 0
    max_ones = 0

    for i in range(len(A)):
        if A[i] == 0:
            zero_count += 1

        while zero_count > B:
            if A[left] == 0:
                zero_count -= 1
            left += 1
        
        max_ones = max(max_ones, i-left + 1)
            
    return max_ones


A = [1, 0, 0, 1, 0, 1, 0, 1, 0, 1]
B = 2

print(maxOnes(A, B))