'''
Created on Jul 24, 2018
Given an array of integers, every element appears twice except for one. Find that single one.
@author: smaiya
'''

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        out = 0
        for num in A:
            out = out^num
        return out

inp = [1, 2, 2, 3, 1]
out = Solution().singleNumber(inp)
print('Single Number which doesnt appear twice = ', out)