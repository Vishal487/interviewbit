def anagrams(A):
    d = dict()
    for i in range(len(A)):
        e = A[i]
        ne = "".join(sorted(e))
        if ne in d:
            d[ne].append(i+1)
        else:
            d[ne] = [i+1]
    ans = []
    for k,v in d.items():
        ans.append(v)
    return ans




    # S = "vishal"
    # sl = ['a', 'b']
    # # print("".join(sl))
    # print("".join(sorted(S)))
    





A = ["cat", "dog", "god", "tca"]
print(anagrams(A))
