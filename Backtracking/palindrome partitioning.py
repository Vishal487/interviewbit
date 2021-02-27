def isPalindrome(s):
    return s == s[::-1]


def partition(A):
    ans = []
    
    def split(A, row):
        if not A:
            ans.append(row)
            return
        for i in range(1, len(A)+1):
            if isPalindrome(A[:i]):
                split(A[i:], row+[A[:i]])
        return

    split(A, [])
    return ans



A = "aab"
print(partition(A))