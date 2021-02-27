def grayCodeUtil(l1, n):
    l2 = l1[::-1]
    for i in range(len(l1)):
        l1[i] = '0' + l1[i]
        l2[i] = '1' + l2[i]
    l1.extend(l2)
    if n == 1:
        return l1  
    return grayCodeUtil(l1, n-1)


def grayCode(A):
    if A == 0:
        return [0]
    if A == 1:
        return [0,1]
        
    l1 = ['0', '1']
    binList = grayCodeUtil(l1, A-1)
    ans = []
    for e in binList:
        ans.append(int(e, 2))
    return ans

def sol2(A):


n = 1
print(grayCode(n))
