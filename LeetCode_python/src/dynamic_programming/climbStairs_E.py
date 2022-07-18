'''
70. Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

'''

class Solution:
    # @param A : integer
    # @return an integer
    def climbStairs(self, A):
        if A == 0:
            return 0
        elif A == 1:
            return 1
        elif A == 2:
            return 2
        (A1, A2) = (2, 1)

        for i in range(3, A+1):
            An = A1+A2
            (A1, A2) = (An, A1)
        return An


a = Solution()
inp = 4
inp = 3
str = a.climbStairs(inp)
print ('Number of ways to climb Stairs = ', str)
