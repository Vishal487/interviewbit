def largestNumber(A):
    mxm_digits = len(str(max(A)))
    l = mxm_digits + 1

    ext_val = []
    ans = ""

    for i in range(len(A)):
        temp = (str(A[i]))*l

        ext_val.append([temp[:l:], A[i]])

    ext_val.sort(key=lambda x : x[0], reverse=True)   

    for e in ext_val:
        ans += str(e[1])

    return ans


A = [3, 30, 34, 5, 9]

print(largestNumber(A))