'''
2301. Match Substring After Replacement

You are given two strings s and sub. You are also given a 2D character array mappings 
where mappings[i] = [oldi, newi] indicates that you may perform the following 
operation any number of times:

Replace a character oldi of sub with newi.
Each character in sub cannot be replaced more than once.

Return true if it is possible to make sub a substring of s by replacing zero or more 
characters according to mappings. Otherwise, return false.

A substring is a contiguous non-empty sequence of characters within a string.

Input: s = "fool3e7bar", sub = "leet", mappings = [["e","3"],["t","7"],["t","8"]]
Output: true
Explanation: Replace the first 'e' in sub with '3' and 't' in sub with '7'.
Now sub = "l3e7" is a substring of s, so we return true.

Solution:
    - Store the mappings in a hashmap
    - Enumerate all substrings of s with the same length as sub, and compare each substring 
    to sub for equality.
    - O(m*n)

Created on July 10, 2022
@author: smaiya
'''
from typing import Dict, Any, List
from collections import defaultdict

class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        map = defaultdict(set)
        for m in mappings:
            map[m[0]].add(m[1])
        
        for i in range(len(s)-len(sub)+1):
            if self.check(s[i:i+len(sub)], sub, map):
                return True
        return False


    def check(self, c1_str, c2_str, map):
        for (c1, c2) in zip(c1_str, c2_str):
            if c1!=c2 and c1 not in map[c2]:
                return False
        return True


s = "fooleetbar"
sub = "f00l"
mappings = [["o","0"]]

ans = Solution().matchReplacement(s, sub, mappings)
