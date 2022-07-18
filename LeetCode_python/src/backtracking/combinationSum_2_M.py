'''
40. Combination Sum II

Question: Given a collection of candidate numbers (candidates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sums to target.
Each number in candidates may only be used once in the combination.

Solution: Same procedure as combinationSum. Differences
    - Since no repetition of numbers, start from index = i+1
    - To avoid duplicate entires, do not call self.dfs on the same number. 
        - Sort the candidates and check with the previous element for duplication before calling self.dfs

Created on Apr 5, 2019

@author: smaiya
'''


class Solution:
    def combinationSum2(self, candidates, target):
        result = []
        candidates.sort()
        self.dfs(candidates, 0, target, [], result)
        return result
    
    def dfs(self, nums, index, target, path, result):
        if target==0:
            result.append(path)
            return
        if target<0:
            return
        prev_num = None
        for i in range(index, len(nums)):
            if nums[i] != prev_num:
                self.dfs(nums, i+1, target-nums[i], path+[nums[i]], result)
            prev_num = nums[i]
            
            
inp = [10,1,2,7,6,1,5]
op = Solution().combinationSum2(inp, 8)
print ('Combinations = ', op)