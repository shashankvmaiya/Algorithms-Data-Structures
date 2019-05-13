'''
Created on Jun 30, 2018
You are given an array (zero indexed) of N non-negative integers, A0, A1 ,..., AN-1.
Find the minimum sub array Al, Al+1 ,..., Ar so if we sort(in ascending order) that sub array, 
then the whole array should get sorted.
If A is already sorted, output -1.
@author: smaiya
'''

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def subUnsort(self, A):
        n = len(A)
        A_sorted = sorted(A)
        left_idx, right_idx = 0, n-1
        start_flag = False
        for i in range(n):
            if A_sorted[i] != A[i]:
                if start_flag:
                    right_idx = i
                else:
                    left_idx = i
                    start_flag = True
        
        if start_flag:
            return [left_idx, right_idx]
        else:
            return [-1]


a = Solution()
inp = [1, 3, 2, 4, 5]
inp = [5, 4, 2, 1, 0]
inp = [1, 2, 5, 4, 3]
inp = [2, 1, 3, 4, 5]
inp = [1, 1]
out = a.subUnsort(inp)
print ('Sub Array (L, R) = ', out)
