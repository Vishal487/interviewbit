def lenghtOfLastWord(A):
    n = len(A)
    if n == 0:
        return 0
    res = ""
    for i in range(n-1, -1, -1):
        if A[i] != " ":
            res += A[i]
        elif A[i] == " " and res == "":
            pass
        elif A[i] == " ":
            break
    return len(res)


A = ""

print(lenghtOfLastWord(A))

