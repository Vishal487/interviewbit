def solve(A):
    A.sort(key=lambda x : x[1])
    ans = 1
    curr_end_time = A[0][1]
    for i in range(1, len(A)):
        if curr_end_time < A[i][0] :   # note that curr_end_time <= A[i][0] is wrong bcz we want disjoint intervals
            curr_end_time = A[i][1]
            ans += 1
    return ans




A = [
  [3, 13],
  [7, 7],
  [3, 10],
  [4, 8],
  [7, 8],
  [9, 12],
  [3, 6],
  [7, 12],
  [4, 10],
  [3, 8],
  [5, 11],
  [9, 10],
  [3, 7],
  [4, 4],
  [7, 15],
  [2, 9]
]

print(solve(A))


"""
A = [
       [1, 9]
       [2, 3]
       [5, 7]
     ]

sorted based on end time::
A = [
       [2, 3]
       [5, 7]
       [1, 9]
     ]

"""