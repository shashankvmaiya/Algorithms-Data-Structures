'''
Question: Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.
Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

Solution: Use recursion (similar to combinationSum_2)
    - For each set, append all nums in increasing order as long as the number is not repeated

Created on Apr 7, 2019

@author: smaiya
'''

class Solution:
    def subsetsWithDup(self, nums):
        result = []
        nums.sort()
        self.dfs(nums, 0, [], result)
        return result
    
    def dfs(self, nums, index, subset, result):
        result.append(subset)
        if index==len(nums):
            return
        prev_num = None
        for i in range(index, len(nums)):
            if nums[i] != prev_num:
                self.dfs(nums, i+1, subset+[nums[i]], result)
            prev_num = nums[i]

