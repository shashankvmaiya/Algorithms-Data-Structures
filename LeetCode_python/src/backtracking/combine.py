'''
Created on Jul 8, 2018
Given two integers n and k, return all possible combinations of k numbers out of 1 2 3 ... n.

Make sure the combinations are sorted.
@author: smaiya
'''

class Solution:
    # @param A : integer
    # @param B : integer
    # @return a list of list of integers
    def combine(self, A, B):
        if B == 1:
            result = []
            for i in range(A):
                result.append([i+1])
            return result
        elif A == B:
            result = [list(range(1, A+1))]
            return result
        else:
            result = []
            for i in range(1, A-B+2):
                temp = self.combine(A-i, B-1)
                for j in temp:
                    result.append([i] + [x+i for x in j])
            return result
                


a = Solution()
n, k = 4, 3
out = a.combine(n, k)
print('All Combinations of n and k = ', out)

