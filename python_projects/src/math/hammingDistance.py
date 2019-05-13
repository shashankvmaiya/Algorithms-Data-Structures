'''
Created on Jul 19, 2018

@author: smaiya
'''

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def bitSum(self, n):
        out = 0
        while n!=0:
            out+=n%2
            n = n>>1
        return out
    def hammingDistance(self, A):
        out = 0
        n = len(A)
        for i in range(32):
            count = 0
            for j in range(n):
                count = count+1 if (A[j] & 1<<i) else count
            out += count*(n-count)*2
        return out%1000000007


inp = [0, 1, 1, 0]
inp = [2, 4, 6]
out = Solution().hammingDistance(inp)
print('Hamming Distance = ', out)
