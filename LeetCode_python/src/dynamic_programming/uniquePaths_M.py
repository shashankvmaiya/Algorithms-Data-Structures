'''
62. Unique Paths

Created on Jul 18, 2018

There is a robot on an m x n grid. The robot is initially located at the top-left corner 
(i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). 
The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot 
can take to reach the bottom-right corner.

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

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

