# def isPalindrome(A):     # using extra space 
#     if A < 0:
#         return False
#     else:
#         A = str(A)      # here extra space has been used
#         i = 0
#         j = len(A) - 1
#         while i <= j:      # using 2-pointer technique to check if string is palindrome
#             if A[i] != A[j]:
#                 return False
#             i += 1
#             j -= 1
#         return True

def isPalindrome(A):
    if A < 0:
        return False
    else:
        temp = A
        n = 0
        while A >= 10:
            digit = A % 10
            n = (n*10) + digit
            A = A // 10
        n = (n*10) + A
        return  n == temp




A = 1000000001 
print(isPalindrome(A))