def longestConsecutive(A):
    if len(A) == 0:
        return 0
    d = dict()
    for e in A:
        d[e] = 1
    
    cnt = 1
    max_count = cnt
    prev = A[0]
    i = 0
    while i <= len(A):
        # print(A[i], i)
        if prev + 1 in d.keys():
            cnt += 1
            prev = prev + 1
        else:
            if cnt > max_count:
                max_count = cnt
            cnt = 1
            i += 1
            if i < len(A):
                prev = A[i]
    return max_count

import random
def longestConsecutive_better_TC(A):
        # Create a set with all the values in it
        vals = set()
        for elem in A:
            vals.add(elem)
            
        # Pick a value and keep searching on both sides of array
        # Repeat process until all elements in set are removed
        maxLen = 1
        while len(vals) > 0:
            val = random.sample(vals, 1)[0] # we know the length is greater than 0
            left = val-1
            right = val+1
            curLen = 1
            vals.remove(val) # remove this element since already visited
  
            while left in vals:
                curLen += 1
                vals.remove(left) # remove from the set to avoid visiting again
                left -=1 
            while right in vals:
                curLen += 1
                vals.remove(right)
                right += 1
            maxLen = max(curLen, maxLen)
        return maxLen



A = [100, 4, 200, 1, 3, 2]
print(longestConsecutive(A))
print(longestConsecutive_better_TC(A))

