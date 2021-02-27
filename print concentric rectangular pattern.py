# https://www.interviewbit.com/problems/prettyprint/

A = 4
size = 2*A - 1    # total no. of rows/cols to be printed
ans = [[0 for i in range(size)] for j in range(size)]

for i in range(size):
    for j in range(size):
        if abs(i - (size // 2)) > abs(j - (size // 2)):
            ans[i][j] = abs(i - (size // 2)) + 1
        else:
            ans[i][j] = abs(j - (size // 2)) + 1

for r in ans:
    print(r)