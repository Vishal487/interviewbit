import heapq

def merge(A):
    # return heapq.merge(*A)   # one line solution
    pq=[]
    heapq.heapify(pq)
    output=[]
    for i in range(len(A)):
        heapq.heappush(pq,(A[i][0],i,0))
    while(len(pq)!=0):
        a,b,c = heapq.heappop(pq)
        i=b
        j=c
        output.append(a)
        if(j+1<len(A[i])):
            heapq.heappush(pq,(A[i][j+1],i,j+1))
    return output




A = [  [1, 2, 3],
        [2, 4, 6],
        [0, 9, 10]
    ]
print(merge(A))