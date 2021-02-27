def maxProfit(A):
    profit = 0
    for i in range(1, len(A)):
        if A[i] > A[i-1]:
            profit += A[i]-A[i-1]
    return profit


A = [1,2,3]

print(maxProfit(A))


"""
5 6 10
"""