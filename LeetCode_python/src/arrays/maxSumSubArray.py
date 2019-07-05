'''
Created on Jun 30, 2018
Find out the maximum sub-array of non negative numbers from an array.
A : [1, 2, 5, -7, 2, 3]
The two sub-arrays are [1, 2, 5] [2, 3].
The answer is [1, 2, 5] as its sum is larger than [2, 3]
Tie Breaker: larger segment length, and then minimum starting index
@author: smaiya
'''


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        n = len(A)
        start_idx, end_idx, length, max_sum = -1, -1, -1, -1
        curr_sum, curr_start_idx, curr_length = 0, 0, 0
        for i in range(n):
            if A[i]<0 or i==n-1:
                if i==n-1 and A[i]>=0:
                    curr_sum, curr_length = curr_sum+A[i], curr_length+1
                if curr_sum > max_sum or (curr_sum == max_sum and curr_length > length):
                    start_idx, end_idx, length, max_sum = curr_start_idx, curr_start_idx+curr_length-1, curr_length, curr_sum
                curr_sum, curr_start_idx, curr_length = 0, i+1, 0
            else:
                curr_sum, curr_length = curr_sum+A[i], curr_length+1
        if max_sum < 0:
            return []
        else:
            return A[start_idx:end_idx+1]
            
        

a = Solution()
inp = [1, 2, 5, -7, 2, 3]
inp = [0, 0, 0, -1, 0]
inp = [1, 2, 3, -4, 6, 0, -1, 8, 0, 0, 0]
inp = [1, 2, 3, -4, 6, 0, -1, 6, 0, 0, 0]
inp = [1, 2, 3, -4, 6, 0, -1, 6, 0, 0, -1]
#inp = [-1, -1, -1, -1, -1 ]
out = a.maxset(inp)
print ('Max sum subarray = ', out)


