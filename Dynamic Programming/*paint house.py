def solRecUtil(cost, n, i, csf):

    if n < 0:
        return 0
    csf += cost[n][i]
    if n == 0:
        return csf

    if i == 0:
        return min(solRecUtil(cost, n-1, 1, csf), solRecUtil(cost, n-1, 2, csf))
    elif i == 1:
        return min(solRecUtil(cost, n-1, 0, csf), solRecUtil(cost, n-1, 2, csf))
    else:  # i == 2
        return min(solRecUtil(cost, n-1, 0, csf), solRecUtil(cost, n-1, 1, csf))


def solRec(cost):
    n = len(cost)
    color = 3
    ans = 99999
    for i in range(color):
        curr_cost = solRecUtil(cost, n-1, i, 0)
        if curr_cost < ans:
            ans = curr_cost
    print(ans)
# above recursive solution is not working    


def solve(A):
    n = len(A)
    if n == 0:
        return 0
    # now assuming A[i] represent the total minimum cost to color
    # all the houses till i with all 3 colors :- this makes constant space
    # so A[i][0] represents total minimum cost if 
    # we color ith house with red color
    for i in range(1, n):
        A[i][0] += min(A[i-1][1], A[i-1][2])
        A[i][1] += min(A[i-1][0], A[i-1][2])
        A[i][2] += min(A[i-1][0], A[i-1][1])
    return min(A[-1])


A = [  [3, 3, 3],
       [10, 11, 12]
     ]
print(solve(A))
solRec(A)
