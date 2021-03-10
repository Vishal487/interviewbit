class Solution:
    def intersect(self, A, B):
        # write your code here...
        i = 0
        j = 0
        ans = []
        while i < len(A) and j < len(B):
            if A[i] == B[j]:
                ans.append(A[i])
                i += 1
                j += 1
            elif A[i] < B[j]:
                i += 1
            else:
                j += 1
        return ans




if __name__ == '__main__':
    mysol = Solution()
    # take inputs...
    A = [1,2,3,3,4,5,6]
    B = [3,3,5]
    
    print(mysol.intersect(A, B))
