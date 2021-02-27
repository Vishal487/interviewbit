def solution(A, B):
    i = min(A-1, B-1)
    j = min(8-A, 8-B)
    k = min(8-A, B-1)
    l = min(A-1, 8-B)
    return i+j+k+l

print(solution(4,4))