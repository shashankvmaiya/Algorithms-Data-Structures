'''
Created on Jul 8, 2018
Given a collection of numbers, return all possible permutations.
You can return the answer in any order.

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

@author: smaiya
'''

class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        n = len(A)
        if n == 1:
            return [A]
        else:
            result = []
            for i in range(n):
                temp = self.permute(A[:i] + A[i+1:])
                for j in temp:
                    result.append([A[i]] + j)
            return result

a = Solution()
inp = [1, 2, 3, 4]
out = a.permute(inp)
print('All Permutations of input = ', out)
