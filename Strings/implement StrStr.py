def strStr(A, B):
    # find B in A
    alen = len(A)
    blen = len(B)
    if blen == 0:
        return -1
    if alen == 0 and blen == 0:
        return -1
    
    if blen > alen:
        return -1
    
    st = B[0]
    res = -1
    for i in range(alen):
        if A[i] == st and A[i:i+blen] == B:
            res = i
            break
    return res

    



B = "vishal"
A = ""
print(strStr(A, B))
