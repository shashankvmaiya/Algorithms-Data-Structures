'''
Created on Jul 24, 2018
Given an array of N integers, find the pair of integers in the array which have minimum XOR value.
Report the minimum XOR value.
Input 
0 2 5 7 
Output 
2 (0 XOR 2) 
@author: smaiya
'''
class Solution:
    # @param A : list of integers
    # @return an integer
    def findMinXor(self, A):
        A_sorted = sorted(A)
        min_xor = None
        for i in range(1, len(A)):
            min_xor = A_sorted[i]^A_sorted[i-1] if min_xor is None or min_xor>A_sorted[i]^A_sorted[i-1] else min_xor
        return min_xor


inp = [0, 2, 5, 7]
inp = [0, 4, 7, 9]
out = Solution().findMinXor(inp)
print('Min XOR Value = ', out)
