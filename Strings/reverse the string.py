def sol2(A):   # using in-built methods
    str_list = list(A.split())
    return " ".join(str_list[::-1])


def customReverse(A):
    str_list = []
    i = 0
    word = ""
    while i < len(A):
        if A[i] == " " and A[i-1] != " " and i!=0:   # word is completed
            str_list.append(word)
            word = ""
        elif A[i] != " ":
            word += A[i]
        i += 1

    if word != "":
        str_list.append(word)

    return " ".join(str_list[::-1])




A = " the   sky is    blue. "
print(customReverse(A))
print(sol2(A))