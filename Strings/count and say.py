def findNext(prev):
    # print("prev : ", prev)
    val = ""
    count = 1
    for i in range(1, len(prev)):
        if prev[i-1] == prev[i]:
            count += 1
        else:
            val = val + str(count) + str(prev[i-1])
            count = 1
    val = val + str(count) + str(prev[-1])
    # print("val : ", val)
    return val


# we can do even better .... actually we don't need this array we can use variables instead to store previous value
def countAndSay(n):
    arr = ["1", "11", "21", "1211", "111221"]
    if n<=5:
        return arr[n-1]
    for i in range(n-5):
        val = findNext(arr[-1])
        arr.append(val)
    # print(arr)
    return arr[-1]



n = 40
print(countAndSay(n))



"""
1 2 11
11 12 21  # 5

111 22 1
31 22 11  # 6

3 1 22 11
13 11 22 21  # 7
"""