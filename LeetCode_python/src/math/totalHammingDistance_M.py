'''
477. Total Hamming Distance
The Hamming distance between two integers is the number of positions at which the 
corresponding bits are different.

Given an integer array nums, return the sum of Hamming distances between all the pairs 
of the integers in nums.

Input: nums = [4,14,2]
Output: 6
Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
showing the four bits relevant in this case).
The answer will be:
HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.

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
    def totalHammingDistance(self, A):
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
