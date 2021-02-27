# def solve(A):
#     B = []
#     queue = []
#     for e in A:
#         if len(B) == 0:
#             queue.append(e)
#             B.append(e)
#         else:
#             if len(queue) == 0:
#                 B.append('#')
#                 queue.append(e)
#             elif queue[0] == e:
#                 queue.pop(0)
#                 if len(queue) != 0:
#                     B.append(queue[0])
#                 else:
#                     B.append('#')
#             else:
#                 queue.append(e)
#                 B.append(queue[0])
#     return "".join(B)

# def solve(A):
#     B = []
#     queue = []
#     for e in A:
#         if len(B) == 0:
#             queue.append(e)
#             B.append(e)
#         else:
#             if e not in queue:
#                 queue.append(e)
#                 B.append(queue[0])
#             else:
#                 ind = queue.index(e)
#                 queue.pop(ind)
#                 if len(queue) != 0:
#                     B.append(queue[0])
#                 else:
#                     B.append('#')
            
#     return "".join(B)


def solve(A):
    B = [A[0]] 
    d = dict()
    d[A[0]] = 1
    queue = [A[0]]
    for e in A[1:]:
        queue.append(e)
        try:
            d[e] += 1
        except:
            KeyError
            d[e] = 1

        while len(queue) != 0 and d[queue[0]] != 1:
            queue.pop(0)
        if len(queue) != 0:
            B.append(queue[0])
        else:
            B.append('#')

    return "".join(B)
    
    
    




A = "jyhrcwuengcbnuchctluxjgtxqtfvrebveewgasluuwooupcyxwgl"
print(solve(A))


"""
jpxvxivxkkthvpqhhh juzhkegnzqr iokhsgea
jjjjjjjjjjjjjjjjjj iiiiiiiiiii xxxxxxxx
jjjjjjjjjjjjjjjjjj iiiiiiiiiii tttttttt
"""


"""
jyhrcwuengcbnuchctluxjgtxqtfvrebveewgasluuwooupcyxwgl
jjjjjjjjjjjjjjjjjjjjj yyyyyyyyyyyyyyyyyyyyyyyyyyy hhhhh
jjjjjjjjjjjjjjjjjjjjj yyyyyyyyyyyyyyyyyyyyyyyyyyy qqqqq
"""