def solve(A):
    ans = 0
    n = len(A)
    for i in range(n, -1, -1):
        if A[:i] == (A[:i])[::-1]:
            ans = n-i
            break
    return ans 

def solveUsingLpsArray(A):
    s = A + '#' + A[::-1]
    n = len(s)
    lps = [0] * n   # lps[0] is always 0
  
    l = 0
     
    i = 1
    while (i < n) :
        if (s[i] == s[l]) :
            l = l + 1
            lps[i] = l
            i = i + 1
         
        else :
            if (l != 0) :
                l = lps[l-1]
            else :
                lps[i] = 0
                i = i + 1
    return len(A) - lps[-1]




A = "AACECAAAA"
print(solve(A))
print(solveUsingLpsArray(A))

