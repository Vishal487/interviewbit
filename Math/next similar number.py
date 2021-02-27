def nextSmallest(A):
    n = len(A)
    number = list(str(A))
    for i in range(n-1,0,-1): 
        if number[i] > number[i-1]: 
            x = number[i-1] 
            smallest = i 
            for j in range(i+1,n): 
                if number[j] > x and number[j] < number[smallest]: 
                    smallest = j 

            number[smallest],number[i-1] = number[i-1], number[smallest] 
            number[i:] = sorted(number[i:]) 
            return "".join(number)
    
    return -1



A = "218765"
print(nextSmallest(A))