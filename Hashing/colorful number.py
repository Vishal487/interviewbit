def product(numStr):
    p = 1
    for e in numStr:
        p = p * int(float(e))
    return p
    

def colorful(num):
    numStr = str(num)
    lst = []
    for i in range(len(numStr)):
        for j in range(i, len(numStr)):
            lst.append(numStr[i:j+1])
    # print(lst)
    # for ns in lst:
    #     print(product(ns))
    d = dict()
    for ns in lst:
        pr = product(ns)
        print(pr)
        if pr in d.keys():
            # print(ns,pr)
            print("hi")
            return 0
        else:
            d[pr] = True
    return 1

A = 3245574821054845410
print(colorful(A))
