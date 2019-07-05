'''
Created on Jul 19, 2018
You are given two positive numbers A and B. You need to find the maximum valued integer X such that
X divides A i.e. A % X = 0
X and B are co-prime i.e. gcd(X, B) = 1
@author: smaiya
'''
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, A, B):
        if A==B:
            return A
        elif A>B:
            return self.gcd(A-B*max(int(A/B-1), 1), B)
        else:
            return self.gcd(A, B-A*max(1, int(B/A-1)))
    
    def cpFact(self, A, B):
        gcd = self.gcd(A, B)
        while gcd != 1:
            A = int(A/gcd)
            gcd = self.gcd(A, B)
        return A
        



a, b = 10001, 2
out = Solution().cpFact(a, b)
print('Largest Co prime Divisor = ', out)