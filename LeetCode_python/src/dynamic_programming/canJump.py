'''
Question: Given an array A = [3, 2, 1, 0, 4] where ai determines max jump length. Can you reach the last index. 
For the above example, we will get stuck up at idx = 3 where ai = 0

Solution: Dynamic Programming
D(i) = x ==> Max remaining steps at ith idx = x
D(n) = 0 ==> End cannot be reached

D(i) = max(D(i-1)-1, A[i-1]-1) 
'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def canJump(self, A):
        n = len(A)
        if n == 0:
            return 0
        elif n==1:
            return 1
        D1 = A[0]
        for i in range(1, n):
            Dn = max(D1-1, A[i-1]-1)
            if Dn<0:
                return 0
            D1 = Dn
        return 1 if Dn>=0 else 0


a = Solution()
inp = [3, 2, 1, 0, 4]
inp = [5, 0, 0, 0, 0, 1]
inp = [5, 0, 0, 0, 0, 0, 1]
inp = [2, 3, 1, 1, 4]
inp = [0, 10, 0]
str = a.canJump(inp)
print ('Can Jump = ', str)
