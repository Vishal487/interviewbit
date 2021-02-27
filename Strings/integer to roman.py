def intToRoman(A):
    # if A ==
    num = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
    i = len(num)-1
    # for j in range(len(num)):
    #     if num[j] <= A:
    #         i = j

    ans = []
    while A > 0:
        count = A//num[i]

        while count > 0:
            ans.append(sym[i]) 
            count -= 1
        A = A%num[i] 
        i -= 1

    return "".join(ans)


A = 4
print(intToRoman(A))