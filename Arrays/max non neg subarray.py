

def maxset(A):
    A.append(-1)
    max_sum = -99999
    sub_arr = []
    curr = []
    for i in range(len(A)):
        if A[i] >= 0:
            curr.append(A[i])
        else:
            curr_sum = sum(curr)
            # print("curr_sum: ", curr_sum)
            # print("max_sum: ", max_sum)
            if max_sum < curr_sum:
                max_sum = curr_sum
                sub_arr = curr
            elif max_sum == curr_sum:
                if len(curr) > len(sub_arr):
                    max_sum = curr_sum
                    sub_arr = curr
            curr = []
    return sub_arr



A = [10, -1, 2, 3, -4, 100]
print(maxset(A))