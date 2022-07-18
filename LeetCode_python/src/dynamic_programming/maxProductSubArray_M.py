'''
152. Maximum Product Subarray

Question: Given an integer array nums, find the contiguous subarray within an array 
(containing at least one number) which has the largest product.

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Solution: 
    - let dp1[i] be maximum product ending at index i
    - let dp2[i] be minimum product ending at index i
    then
        - dp1[i] = max(dp1[i - 1]*nums[i], nums[i], dp2[i - 1]*nums[i])
        - dp2[i] = min(dp1[i - 1]*nums[i], nums[i], dp2[i - 1]*nums[i])
    dp2 is used to keep track of the negative product with highest absolute value. 
    If ith element is also negative, then dp2[i-1]*num[i] would be the max value
        
Created on Apr 7, 2019

@author: smaiya
'''

class Solution:
    def maxProduct(self, nums):
        if not nums:
            return 0
        n = len(nums)
        dp1 = [0 for i in range(n)] # Max product if it were to end at i
        dp2 = [0 for i in range(n)] # Min product if it were to end at i
        
        dp1[0], dp2[0] = nums[0], nums[0]
        for i in range(1, n):
            dp1[i] = max(nums[i], nums[i]*dp1[i-1], nums[i]*dp2[i-1])
            dp2[i] = min(nums[i], nums[i]*dp1[i-1], nums[i]*dp2[i-1])
        return max(dp1)


