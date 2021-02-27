def solve(A, B):
    A.sort(reverse=True)
    return A[:B]

import heapq
def sol_using_heap(A, B):
    n = len(A)
    heapq.heapify(A)
    to_remove = n-B
    while to_remove > 0:
        heapq.heappop(A)
        to_remove -= 1
    return list(A)

A = [11, 3, 4, 6]
B = 3
print(solve(A, B))
print(sol_using_heap(A, B))
