'''
Created on Jul 12, 2018

@author: smaiya
'''

class Solution:
    # @param A : integer
    # @return a list of integers
    def grayCode(self, A):
        if A == 1:
            return [0, 1]
        temp = self.grayCode(A-1)
        result = temp + [x+pow(2, A-1) for x in temp[-1::-1]]
        return result


a = Solution()
n=3
out = a.grayCode(n)
print('Gray Code = ', out)
