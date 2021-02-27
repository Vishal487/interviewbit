def noOfSetBits(A):
    count = 0

    while A > 0:     # O(log A)
        count += A%2
        A = A//2

    return count

def sol2(A):    # O(no_of_set_bits)
    count = 0

    while A > 0:
        count += 1
        A = A & (A-1)      # this unset the lowest set bit
    
    return count



A = 12258
print(noOfSetBits(A))
print(sol2)