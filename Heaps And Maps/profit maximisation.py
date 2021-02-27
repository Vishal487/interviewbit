import heapq

def maximizeProfit(A, B):
    for i in range(len(A)):
        A[i] = -A[i]   # bcz in python, only min_heap exist :)
    heapq.heapify(A)

    profit = 0
    for _ in range(B):
        popped = heapq.heappop(A)
        profit += abs(popped)
        heapq.heappush(A, popped+1)
    return profit


A = [1, 4]
B = 2
print(maximizeProfit(A, B))
