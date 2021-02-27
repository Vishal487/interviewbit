"""
    space: O(n) [not accepted :( ]
    time : linear
    traversing the stream sequentially O(1) times.
"""

def repeatedNumber(A):
    d = dict()
    flag = 0
    for e in A:
        if e in d:    # instead we can use try and except statement to avoid searching for "e" in "d"
            flag = 1
            return e
        else:
            d[e] = 1
    if flag == 0:
        return -1


A = [3, 4, 1, 4, 1]

print(repeatedNumber(A))