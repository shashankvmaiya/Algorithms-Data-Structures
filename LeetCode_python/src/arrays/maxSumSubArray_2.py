'''
Question: Given an integer array nums, 
find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Solution: Dynamic Programming
    - Dn = max sum ending at n
    - Dn = nums[i] + max(0, D(n-1))

Created on Apr 5, 2019

@author: smaiya
'''

class Solution:
    def maxSubArray(self, nums):
        if not nums:
            return 0
        max_sum, Dn = nums[0], nums[0]
        for i in range(1, len(nums)):
            Dn = nums[i] + max(0, Dn)
            max_sum = max(max_sum, Dn)
        return max_sum