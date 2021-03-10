def solve(A, B):
    # write your code here...
    n = len(A)
    s = ""
    i = 0
    j = 0
    while i < n:
        temp = ""
        j = i
        while j < n and A[i] == A[j]:
            temp += A[j]
            j += 1
        if len(temp) != B:
            s += temp
        i = j
    return s



if __name__ == '__main__':
    # take inputs...
    A = "aabcd"
    B = 2
    print(solve(A, B))
