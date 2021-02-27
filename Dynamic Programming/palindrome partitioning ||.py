# O(n*3) time solution

def minCuts(A):
    n = len(A)
    dp = [[False for i in range(n)] for j in range(n)]

    for g in range(n):
        i = 0
        j = g
        while j < len(dp):
            if g == 0:
                dp[i][j] = True
            elif g == 1:
                dp[i][j] = A[i]==A[j]
            else:
                if A[i] == A[j] and dp[i+1][j-1]==True:
                    dp[i][j] = True
                else:
                    dp[i][j] = False
            i += 1
            j += 1
    
    storage = [[0 for i in range(n)] for j in range(n)]
    for g in range(n):
        i = 0
        j = g
        while j < len(storage):
            if g == 0:
                storage[i][j] = 0
            elif g == 1:
                if A[i] == A[j]:
                    storage[i][j] = 0
                else:
                    storage[i][j] = 1
            else:
                if dp[i][j]:
                    storage[i][j] = 0
                else:
                    mn = 9999999
                    for k in range(i, j):
                        left = storage[i][k]
                        rit = storage[k+1][j]

                        if left + rit + 1 < mn:
                            mn = left + rit + 1
                    storage[i][j] = mn
            i += 1
            j += 1
    return storage[0][n-1] 



A = "aab"
print(minCuts(A))


"""
aba

  a b a
a T F T
b x T F
a x x T

"""