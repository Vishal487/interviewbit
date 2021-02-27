def isPalindrome(A):
    A = A.lower()
    l = []
    for e in A:
        if (ord(e) <= 122 and ord(e) >= 97) or (ord(e) >= 48 and ord(e) <= 57):
            l.append(e)
    A = "".join(l)
    return A == A[::-1]


def betterSolution(A):
    A = A.lower()
    n = len(A)
    if n == 0:
        return 1
    i = 0
    j = n-1
    while i <= j:
        a = A[i]
        b = A[j]
        if ((ord(a)<=122 and ord(a)>=97) or (ord(a)>=48 and ord(a)<=57)) and  ((ord(b)<=122 and ord(b)>=97) or (ord(b)>=48 and ord(b)<=57)):
            if a != b:
                return 0
            else:
                i += 1
                j -= 1
        elif ((ord(a)<=122 and ord(a)>=97) or (ord(a)>=48 and ord(a)<=57)) and (not ((ord(b)<=122 and ord(b)>=97) or (ord(b)>=48 and ord(b)<=57))):
            j -= 1
        elif (not ((ord(a)<=122 and ord(a)>=97) or (ord(a)>=48 and ord(a)<=57)) ) and ((ord(b)<=122 and ord(b)>=97) or (ord(b)>=48 and ord(b)<=57)):
            i += 1
        else:
            i += 1
            j -= 1
    return 1

def moreBetterSolution(A):
    n = len(A)
    i = 0
    j = n-1
    if n == 0:
        return 1
    while i <= j:
        if A[i].isalnum() and A[j].isalnum():
            if A[i].lower() != A[j].lower():
                return 0
            else:
                i += 1
                j -= 1
        elif not A[i].isalnum():
            i += 1
        elif not A[j].isalnum():
            j -= 1
    return 1


A = "race a car"
print(isPalindrome(A))
print(betterSolution(A))
print(moreBetterSolution(A))

