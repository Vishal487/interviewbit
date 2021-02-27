def singleNumber(A):    # time: O(len(A)) and space: O(1)
    ans = 0
    for e in A:
        ans = ans ^ e
    return ans



A = [1, 2, 2]
print(singleNumber(A))

