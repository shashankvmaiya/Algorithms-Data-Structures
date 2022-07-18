'''
491. Increasing Subsequences

Question: Given an integer array, your task is to find all the different possible increasing subsequences of the given array,
and the length of an increasing subsequence should be at least 2 .
Input: [4, 6, 7, 7]
Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]

Solution: 
    - Use DFS. Call recursively only if the current number >= last number in the current subsequence

Created on May 12, 2019

@author: smaiya
'''


class Solution:
    def findSubsequences(self, nums):
        
        result = []
        self.dfs(0, [], nums, result)
        return result
    
    def dfs(self, idx, subseq, nums, result):
        if len(subseq)>=2: # Add to the result, if the length of subsequence >=2
            result.append(subseq)
        if idx==len(nums):
            return
        
        visited = set() # Ensuring we do not add repeated elements
        for i in range(idx, len(nums)):
            # If subseq is empty, then check all numbers. If not, then add only those numbers that are greater than last subsequence number
            if (nums[i] not in visited) and (not subseq or subseq[-1]<=nums[i]): 
                visited.add(nums[i])
                self.dfs(i+1, subseq+[nums[i]], nums, result)
