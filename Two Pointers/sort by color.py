class Solution:
    def sortColors(self, A):
        # write your code here...
        count_0 = count_1 = count_2 = 0
        for e in A:
            if e == 0:
                count_0 += 1
            elif e == 1:
                count_1 += 1
            else:
                count_2 += 1
        
        for i in range(len(A)):
            if count_0 > 0:
                A[i] = 0
                count_0 -= 1
            elif count_1 > 0:
                A[i] = 1
                count_1 -= 1
            else:
                A[i] = 2
                count_2 -= 1
        return A




if __name__ == '__main__':
    mysol = Solution()
    # take inputs...
    A = [0,1,2,0,1,2]
    
    print(mysol.sortColors(A))
