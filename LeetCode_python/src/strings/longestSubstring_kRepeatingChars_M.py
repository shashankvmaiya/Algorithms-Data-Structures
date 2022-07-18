'''
395. Longest Substring with At Least K Repeating Characters

Question: https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/
Find the length of the longest substring T of a given string (consists of lowercase letters only) 
such that every character in T appears no less than k times.
Input:
s = "ababbc", k = 2
Output:
5
The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.

Solution: 
    - Recursive algo
    - Get a hashmap of all the characters in string
    - If count for a particular character<k, then split the string based on that character
        - max_length = max(longestSubstring(all the substrings formed by the split))

Created on Jun 1, 2019

@author: smaiya
'''

import collections
class Solution:
    def longestSubstring(self, s, k):
        count = collections.Counter(s)
        for c in count:
            if count[c]<k:
                return max(self.longestSubstring(sub, k) for sub in s.split(c))
        return len(s)
