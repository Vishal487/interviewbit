def power(x, n, d):
    return pow(x, n, d)
    




x = 2
n = 3
d = 3
print(power(x, n, d))


"""
3^8 = 3*3*3*3*3*3*3*3 -> 7 multiplication
better way
    81 = 3*3*3*3             -> 3 multiplication
    and then 3^8 = 81 * 81   -> 1 multiplication
similarly we can do something similar to binary search
"""