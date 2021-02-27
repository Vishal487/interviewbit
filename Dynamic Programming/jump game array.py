def canJump(A):
    reachable = 0
    for i in range(len(A)):
        if reachable >= i:
            reachable = max(reachable, i+A[i])
    return int(reachable >= len(A)-1)



A = [3,2,1,0,4]
print(canJump(A))