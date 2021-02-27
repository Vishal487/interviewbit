from collections import deque


def letterCombinationsUtil(number, n, table):
    list = []
    q = deque()
    q.append("")
 
    while len(q) != 0:
        s = q.pop()
        if len(s) == n:
            list.append(s)
        else:
            for letter in table[number[len(s)]]:
                q.append(s + letter)
 
    return list

def letterCombinations(A):
    number = []
    for e in A:
        number.append(int(float(e)))
    n = len(number)
    table = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

    list = letterCombinationsUtil(number, n, table)


    return list[::-1]





A = "2"
print(letterCombinations(A))
