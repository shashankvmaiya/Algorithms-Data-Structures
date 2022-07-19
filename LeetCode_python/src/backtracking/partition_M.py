'''
131. Palindrome Partitioning

Given a string s, partition s such that every substring of the partition is a palindrome. 
Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Solution
    - Use dfs
    - Start searching for a palindrome from the start
    - If found add it into a temp list and search for the next starting from the next index
    - Add the temp list into the final result array if the string ending with the last index is a palindrome

Created on July 18, 2022
@author: smaiya
'''
from typing import Dict, Any, List
from collections import defaultdict

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.result = []
        self.n = len(s)
        self.dfs(s, 0, [])
        return self.result

    def is_palindrome(self, s):
        for i in range(len(s)):
            if s[i] != s[len(s)-i-1]:
                return False
        return True

    def dfs(self, s, idx, temp_result):
        if idx==self.n:
            self.result.append(temp_result.copy())
            return
        
        for i in range(idx+1, self.n+1):
            sub = s[idx:i]
            if self.is_palindrome(sub):
                temp_result.append(sub)
                self.dfs(s, i, temp_result)
                temp_result.pop()


s = "aab"
ans = Solution().partition(s)
