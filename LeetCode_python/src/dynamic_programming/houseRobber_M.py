'''
198. House Robber

Question: You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, 
the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically 
contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob 
tonight without alerting the police.
Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
             
Solution: Maintain 2 entries at every n
    1. max loot including the current house = nums[i] + loot excluding the previous house
    2. max loot excluding the current house = max(loot including, excluding the previous house)

Created on Apr 21, 2019

@author: smaiya
'''


class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        n = len(nums)
        if n==1:
            return nums[0]
        
        dn = [nums[0], 0]
        for i in range(1, n):
            include = nums[i]+dn[1]
            exclude = max(dn)
            dn = [include, exclude]
        return max(dn)

