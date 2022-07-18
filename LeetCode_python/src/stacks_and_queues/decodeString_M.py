'''
394. Decode String

Question: Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. 
Note that k is guaranteed to be a positive integer.
s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

Solution: Use stack

Created on May 12, 2019

@author: smaiya
'''

class Solution:
    def decodeString(self, s):
        
        num, pattern = '', ''
        num_stack, pattern_stack = [], []
        for c in s:
            if c.isdigit():
                num+=c
            if c.isalpha():
                pattern+=c
            if c=='[':
                num_stack.append(num)
                pattern_stack.append(pattern)
                num, pattern = '', ''
            if c==']':
                n = num_stack.pop()
                p = pattern_stack.pop()
                pattern = p+pattern*int(n)
                
        return pattern
