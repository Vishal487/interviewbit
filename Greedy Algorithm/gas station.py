def canCompleteCircuit(A, B):
    start = 0
    end = 0
    n = len(A)
    balance = A[start] - B[start]
    prev_val = 0

    while end != n-1 and start != n-1:
        if balance >= 0:
            end = (end + 1)%n
            balance += A[end]-B[end]
        else:
            start = end+1
            end = start
            prev_val += balance
            balance = A[start]-B[start]
    balance += prev_val
    return start if balance >= 0 else -1



A =  [1, 2]
B =  [2, 1]
print(canCompleteCircuit(A, B))
