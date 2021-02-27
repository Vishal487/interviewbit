def plusOne(A):
    A = [str(e) for e in A]
    s = "".join(A)
    num = int(s)
    num += 1
    s = str(num)
    return list(s)


A = [0,0,0,1,2,3,4,5]
print(plusOne(A))
