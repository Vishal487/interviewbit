class Solution:
    def threeSum(self, A):
        # write your code here...
        i = 0,
        ans = []
        A.sort()
        for i in range(len(A) - 2):
            l, r = i+1, len(A) - 1
            while l < r:
                if (A[i] + A[l] + A[r]) == 0:
                    ans.append([A[i], A[l], A[r]])
                    l += 1
                    r -= 1
                elif A[i] + A[l] + A[r] > 0:
                    r -= 1
                else:  # if A[i] + A[l] + A[r] < 0:
                    l += 1
        ans.sort()
        uniq = []
        for i in range(len(ans)):
            if ans[i] not in uniq:
                uniq.append(ans[i])
        return uniq



if __name__ == '__main__':
    mysol = Solution()
    # take inputs...
    A = [-1,0,1,2,-1,-4]
    
    print(mysol.threeSum(A))
