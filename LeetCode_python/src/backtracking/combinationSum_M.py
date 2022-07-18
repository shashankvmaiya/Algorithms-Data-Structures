'''
39. Combination Sum

Question: Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sums to target.
The same repeated number may be chosen from candidates unlimited number of times.

Solution: Use recursion. 
    - For each path, append all nums in increasing order as long as < target

Created on Apr 5, 2019

@author: smaiya
'''

class Solution:
    def combinationSum(self, candidates, target):
        result = []
        candidates.sort()
        self.dfs(candidates, 0, target, [], result)
        return result
    
    def dfs(self, nums, index, target, path, result):
        if target<0:
            return
        if target==0:
            result.append(path)
            return
        # extend the current path to all other possible combinations 
        for i in range(index, len(nums)):
            self.dfs(nums, i, target-nums[i], path+[nums[i]], result)


inp = [2, 3, 6, 7]
op = Solution().combinationSum(inp, 7)
print ('Number of Combinations = ', op)