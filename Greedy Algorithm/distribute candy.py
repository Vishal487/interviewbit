def candy(A):
    if len(A) == 1:
        return 1
    change_occured = True
    candies = [1 for i in range(len(A))]
    while change_occured:
        change_occured = False
        # print("candies : ", candies)
        for i in range(len(A)):
            # print("i: ", i)
            if i == 0:
                if A[i] > A[i+1]:
                    if candies[i] <= candies[i+1]:
                        candies[i] += 1
                        change_occured = True
            elif i == len(A)-1:
                if A[i] > A[i-1]:
                    if candies[i] <= candies[i-1]:
                        candies[i] += 1
                        change_occured = True
            else:
                if A[i] > A[i-1]:
                    if candies[i] <= candies[i-1]:
                        candies[i] += 1
                        change_occured = True
                if A[i] > A[i+1]:
                    if candies[i] <= candies[i+1]:
                        candies[i] += 1
                        change_occured = True
    # print(candies)
    return sum(candies)



A = [1]
print(candy(A))





"""
[1, 5, 2, 1]
 1  1  1  1
    1  1  
"""