'''
Created on Jul 20, 2018
Reverse digits of an integer.
Return 0 if the result overflows and does not fit in a 32 bit signed integer
@author: smaiya
'''
class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, A):
        max_positive = 2**31-1
        min_negative = -2**31
        A_str = str(A)
        if A>0:
            A_rev = int(A_str[::-1])
        else:
            A_rev = -int(A_str[:0:-1])
        if A_rev>max_positive or A_rev<min_negative:
            return 0
        else:
            return A_rev


inp = 123
inp = -123
inp = 2**31
out = Solution().reverse(inp)
print('Reverse Integer = ', out)
