'''
Question: Minimum number of characters to make a string a palindrome provided it can
be inserted ONLY in the beginning of the string

Solution: O(n)
Starting from the entire string, keep clipping the last element one by one and checking if the resulting string is a palindrome
Palindrome check: if string = string[::-1]

'''
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        n = len(A)
        for i in range(n,-1,-1):
            if self.is_palindrome(A[:i]):
                break
        return n-i

    def is_palindrome(self, str):
        str_rev = str[::-1]
        if str_rev == str:
            return True
        else:
            return False

a = Solution()
inp = 'zrzbmnmgqoo'
str = a.solve(inp)
print ('Minimum length of string for Palindrome = ', str)
