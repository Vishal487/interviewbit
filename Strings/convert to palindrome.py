def solve(A):
    # write your code here...
    left = 0
    right = len(A)-1
    count = 0
    while left < right:
        if A[left] == A[right]:
            left += 1
            right -= 1
        elif A[left+1] == A[right]:
            count += 1
            left += 1
        elif A[left] == A[right-1]:
            count += 1
            right -= 1
        else:
            return 0
        
        if count >= 2:
                return 0
    if (count == 1) or ( count == 0 and left == right):
        return 1
    return 0



if __name__ == '__main__':
    # take inputs...
    A = "abcba"
    
    print(solve(A))
