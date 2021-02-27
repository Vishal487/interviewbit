def convertToTitle(A):
    alphabets = [chr(x) for x in range(ord('A'), ord('Z') + 1)] 
    res = ""
    while A > 26:
        rem = A%26     # 1 1 
        if rem == 0:
            res += alphabets[25]
            A -= 25
            A = A//26 
        else:
            res += alphabets[rem-1]    #A A 
            A = A//26    # 27 1
        
    res += alphabets[A-1]

    return res[::-1]


A = 943566
print(convertToTitle(A))

"""
 rem : 0 21 17
 res : Z
 A   : .. 36291 1395 53

# AAA -> 703

# AA
# 50 -> AX

"""