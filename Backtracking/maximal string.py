def swap(string, i, j):
 
    return (string[:i] + string[j] +
            string[i + 1:j] +
            string[i] + string[j + 1:])
 

def findMaximum(string, k, maxm):
    if k == 0:
        return
    n = len(string)

    for i in range(n - 1):
         for j in range(i + 1, n):
            if string[i] < string[j]:
                string = swap(string, i, j)
                if string > maxm[0]:
                    maxm[0] = string
                findMaximum(string, k - 1, maxm)
                string = swap(string, i, j)
 



def solve(A, B):
    mxm = [A]
    findMaximum(A, B, mxm)
    return int(float(mxm[0]))
    



A = "2488"
B = 2
print(solve(A, B))
