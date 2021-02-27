def longestPalindrome(A):
    res = ""
    n = len(A)
    for i in range(n):
        for j in range(i, n):
            curr = A[i:j+1]
            if curr == curr[::-1] and len(curr) > len(res):
                res = curr
    return res


def dp_solution(st):   # gfg
    n = len(st) 
    table = [[0 for x in range(n)] for y
                          in range(n)] 
    
    maxLength = 1
    i = 0
    while (i < n) :
        table[i][i] = True
        i = i + 1

    start = 0
    i = 0
    while i < n - 1 :
        if (st[i] == st[i + 1]) :
            table[i][i + 1] = True
            start = i
            maxLength = 2
        i = i + 1

    k = 3
    while k <= n :
        # Fix the starting index
        i = 0
        while i < (n - k + 1) :
            j = i + k - 1
            if (table[i + 1][j - 1] and
                      st[i] == st[j]) :
                table[i][j] = True
     
                if (k > maxLength) :
                    start = i
                    maxLength = k
            i = i + 1
        k = k + 1
    end = start + maxLength - 1
    return st[start: end+1]




A = "abalpoicdc"
print(longestPalindrome(A))
print(dp_solution(A))
