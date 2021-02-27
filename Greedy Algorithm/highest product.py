def maxp3(A):
    A.sort()
    m1 = A[-1]
    m2 = A[-2]
    m3 = A[-3]
    
    A.sort(key=lambda x : -x)

    max_neg1 = A[-1]
    max_neg2 = A[-2]

    ans1 = max(m1, m2, m3)*max_neg1*max_neg2
    ans2 = m1*m2*m3

    return max(ans1, ans2)


A = [ 0, -1, 3, 100, -70, -50 ]
print(maxp3(A))
