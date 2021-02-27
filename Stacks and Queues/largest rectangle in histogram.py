def largestReactangleArea(A):    # TLE
    n = len(A)
    left = []
    right = []

    for i in range(n):
        if len(left) == 0:
            left.append(0)
        else:
            cnt = 0
            j = i-1
            while j >=0 and A[j]>=A[i] :
                cnt += 1
                j -= 1
            left.append(cnt)
    # print(left)

    for i in range(n-1, -1, -1):
        if len(right) == 0:
            right.append(0)
        else:
            cnt = 0
            j = i+1
            while j < n and A[i] <= A[j]:
                cnt += 1
                j += 1
            right.append(cnt)
    right = right[::-1]
    # print(right)


    ans = 0
    for i in range(n):
       ca = (left[i] + right[i] + 1)*A[i]
       ans = max(ans, ca)
    return ans



A = [0]
print(largestReactangleArea(A))
