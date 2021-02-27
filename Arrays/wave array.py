def wave_array(A):
    A.sort()
    i = 0
    while i < len(A) - 1:
        A[i], A[i+1] = A[i+1], A[i]
        i += 2
    
    return A


A = [1, 2, 3, 4]
print(wave_array(A))