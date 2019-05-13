'''
Created on Jul 19, 2018

@author: smaiya
'''

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, A, B):
        if A==0:
            return B
        if B==0:
            return A
        if B>A:
            A, B = B, A 
        while A%B != 0:
            A, B = B, A%B
        return B


a, b = 100, 10
a, b = 6, 9
out = Solution().gcd(a, b)
print('Largest Co prime Divisor = ', out)