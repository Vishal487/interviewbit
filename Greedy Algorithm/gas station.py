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


"""
HINT:
Try to find the relation between sum of gas and sum of cost for solution to exist.

When will you shift your starting point from 0?
Do you really need to cover every starting point? How can you use answer of above question to optimize this part?


Solution Approach:
The bruteforce solution should be obvious. Start from every i, and check to see if every point is reachable with the gas available. Return the first i for which you can complete the trip without the gas reaching a negative number.
This approach would however be quadratic.

Lets look at how we can improve.
1) If sum of gas is more than sum of cost, does it imply that there always is a solution ?
2) Lets say you start at i, and hit first negative of sum(gas) - sum(cost) at j. We know TotalSum(gas) - TotalSum(cost) > 0. What happens if you start at j + 1 instead ? Does it cover the validity clause for i to j already ?

"""

def sol2(A, B):
    sumo=0
    fuel=0
    start=0
    for i in range(len(gas)):
        sumo = sumo + (gas[i] - cost[i])
        fuel = fuel + (gas[i] - cost[i])
        if fuel<0:
            fuel=0
            start=i+1
    if sumo>=0:
        return (start%len(gas))
    else:
        return -1



A =  [1, 2]
B =  [2, 1]
print(canCompleteCircuit(A, B))
