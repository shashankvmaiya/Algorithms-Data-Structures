'''
190. Reverse Bits

Created on Jul 24, 2018
Reverse bits of an 32 bit unsigned integer
00000000000000000000000000000011 
=>        11000000000000000000000000000000
@author: smaiya
'''
class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverseBits(self, A):
        out = 0
        for i in range(32):
            out+=((A&(1<<i))>>i)*(1<<(31-i))
        return out

inp = 3
out = Solution().reverseBits(inp)
print('Bit Reversed = ', out)