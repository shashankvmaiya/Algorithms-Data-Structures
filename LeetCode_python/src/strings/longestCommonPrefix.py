'''
Question: Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
Input: ["flower","flow","flight"]
Output: "fl"

Solution: From i to range(min_len_strings) 
    - Check if length(set(characters in each position)) == 1. If not, then break


Created on Apr 5, 2019

@author: smaiya
'''
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        
        min_len = min([len(s) for s in strs])
        match_idx = 0
        for i in range(min_len):
            chars = [s[i] for s in strs]
            if len(set(chars))>1:
                break
            match_idx+=1
        return strs[0][:match_idx]
    
inp = ["flower","flow","flight"]
op = Solution().longestCommonPrefix(inp)
print ('Longest Common string = ', op)