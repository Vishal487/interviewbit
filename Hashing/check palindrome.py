def canMakePalindrome(A):
    d = dict()
    for e in A:
        try:
            d[e] += 1
        except:
            KeyError
            d[e] = 1
    odd_count = 0
    for key,val in d.items():
        if val % 2 == 0:
            pass
        else:
            odd_count += 1
    if odd_count > 1:
        return 0
    return 1


A = "abaaa"
print(canMakePalindrome(A))


"""
yzfbzbyyrurquqf
y 3
z 2
f 
"""