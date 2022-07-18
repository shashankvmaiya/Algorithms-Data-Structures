'''
Question: Given an array A = [3, 2, 1, 0, 4] where ai determines max jump length. What is the minimum number 
of steps to reach the end

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. 
Jump 1 step from index 0 to 1, then 3 steps to the last index.

Solution: Dynamic Programming : O(sum(n))
D(i) = x ==> Minimum number of steps to reach ith index
D(i+1) = min( D(i)&A(i)>0, D(i-1)&A(i-1)>1, D(i-2)&A(i-2)>2 ...)

    - Start from the A[0]: All indices till A[0]-1 can be reached in 1 step. D(0) to D(A[0]-1) = 1
    - A[1]: All indices till 1+A[1]-1 can be reached in min(2, Di) steps. Di = 1 if it has been visited by the first 
and so on
'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def jump(self, A):
        n = len(A)
        if n < 2:
            return 0
        if A[0]>=n-1:
            return 1
        # Dn contains the minimum number of steps to reach n
        Dn = [float('inf')]*n
        for i in range(A[0]):
            Dn[i+1] = 1
        for i in range(1, n-1):
            steps = A[i]
            if Dn[i] == float('inf'):
                return -1
            elif i+steps>=n-1:
                return Dn[i]+1
            for j in range(steps):
                Dn[i+j+1] = min(Dn[i]+1, Dn[i+j+1])
        return -1



a = Solution()

inp = [5, 0, 0, 0, 0, 1]
inp = [5, 0, 0, 0, 0, 0, 1]
inp = [2, 3, 1, 1, 4]
inp = [0, 10, 0]
inp = [3, 2, 1, 0, 4]
inp = [2, 3, 1, 1, 4]
inp = [0]
inp = [1, 0, 10, 2, 4, 5]

str = a.jump(inp)
print ('Min Number of Jumps = ', str)
