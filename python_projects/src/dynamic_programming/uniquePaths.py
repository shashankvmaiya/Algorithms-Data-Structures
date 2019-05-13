'''
Created on Jul 18, 2018

@author: smaiya
'''

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePaths(self, A, B):
        grid = [[0]*B for x in range(A)]
        grid[0][0]=1
        for i in range(A):
            for j in range(B):
                if i+1<A:
                    grid[i+1][j]+=grid[i][j]
                if j+1<B:
                    grid[i][j+1]+=grid[i][j]
        return grid[A-1][B-1]


a = Solution()
m, n = 5, 2
out = a.uniquePaths(m, n)
print('out = ', out)

