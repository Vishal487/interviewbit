def solve(A):    # not correct XXX
    A.sort(key=lambda x : x[1])
    ans = []
    for interval in A:
        stime = interval[0]
        etime = interval[1]
        for i in range(len(ans)-1, -1, -1):
            if ans[i] <= stime:
                ans[i] = etime
                break
        else:
            ans.append(etime)
    # for e in A:
    #     print(e)
    # print(ans)
    return len(ans)

def sol2(A):    # O(n^2) time
    A.sort(key=lambda x:(x[0],x[1]))
    n = 0
    while A:
        n += 1
        finish = A[0][1]
        A.pop(0)
        i = 0
        while i < len(A):
            if A[i][0] >= finish:
                finish = A[i][1]
                A.pop(i)
            else:
                i += 1
    return n

def sol3(A):   # O(n) time and O(n) space
    d = dict()
    for interval in A:
        s = interval[0]
        e = interval[1]

        if s in d.keys():
            d[s] += 1
        else:
            d[s] = 1
        if e in d.keys():
            d[e] -= 1
        else:
            d[e] = -1
    
    cnt = 0
    ans = 0
    # print(d)
    for key,val in d.items():
        cnt += val
        ans = max(ans, cnt)
    return ans


def sol4(A):   # O(n log n) time and O(n) space
    start = [x[0] for x in A]
    end = [x[1] for x in A] 
    start.sort()
    end.sort()

    max_room = 1
    needed_room = 1

    i = 1
    j = 0
    while i<len(start) and j < len(end):
        if start[i] < end[j]:
            max_room += 1
            i += 1
        else:
            max_room -= 1
            j += 1
        needed_room = max(needed_room, max_room)
    return needed_room
    


A = [   [7, 10], 
        [4, 19], 
        [19, 26], 
        [14, 16], 
        [13, 18], 
        [16, 21]
    ]



# print(solve(A))
# print(sol2(A))
# print(sol3(A))
print(sol4(A))

"""
[7, 10] - a
[14, 16] - b
[13, 18] - c
[4, 19] - d
[16, 21] - e
[19, 26] - f

ans : [21, 18, 19]
      [a]  [c] [d]
      [b]
      [e]
"""




"""
e.g. 1
    5 10
    15 20
    0 30

e.g. 2
    2 11 - 1
    5 13 - 2
    4 15 - 3
    1 18 - 4
    18 23 - 4
    15 29 - 3
"""

"""
e.g. 3
    1 2
    2 3
"""