def convert(A, B):
    if B == 1:
        return A
    l = len(A)
    arr = ["" for x in range(B)]
    row = 0
    for i in range(l):
        arr[row] += A[i]
        if row == B-1:
            down = False
        elif row == 0:
            down = True

        if down:
            row += 1
        else:
            row -= 1
    return "".join(arr)



A = "PAYPALISHIRING"
B = 3
print(convert(A, B))



"""
abcdefghijklm

a   e   i   m
 b d f h j l
  c   g   k

a     g     m 
 b   f h   l
  c e   i k
   d     j

a       i
 b     h j   
  c   g   k
   d f     l
    e       m

"""