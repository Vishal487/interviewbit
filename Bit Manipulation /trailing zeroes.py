def countTrailingZeros(A):   # O(log A)
    count = 0
    while A > 0:
        bit = A%2
        A = A//2
        if bit == 0:
            count += 1
        else:
            break
    return count







A = 8
print(countTrailingZeros(A))