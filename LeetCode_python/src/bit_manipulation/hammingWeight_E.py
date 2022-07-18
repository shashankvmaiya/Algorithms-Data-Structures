'''
191. Number of 1 Bits

Created on Jul 24, 2018
Write a function that takes an unsigned integer and returns the number of 1 bits it has.

@author: smaiya
'''
class Solution:
    # @param A : integer
    # @return an integer
    def hammingWeight(self, A):
        out = 0
        for i in range(32):
            out+=(A&(1<<i))>>i
        return out


inp = 11
out = Solution().hammingWeight(inp)
print('Number of 1 bits = ', out)