'''
20. Valid Parentheses

Question: 
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
    - Open brackets must be closed by the same type of brackets.
    - Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Solution: 
    - Use a stack. 
        - Add if it is open brace. 
        - Pop if it is a close brace. 
    - Use a dictionary with open brace as keys and close brace as values
    - Corner cases:
        - Stack has to be empty at the end (Braces shouldnt be left open)
        - Stack should not be empty when we are popping (Trying to close more braces than those that have been opened)
    
Created on Apr 5, 2019

@author: smaiya
'''

class Solution:
    def isValid(self, s: str) -> bool:
        if s is None:
            return True
        mapping = {'(':')', '[':']', '{':'}'}
        stack = []
        for brace in s:
            if brace in mapping:
                stack.append(brace)
            else:
                if stack:
                    last_brace = stack.pop()
                else: # Closing more braces than those that have been opened
                    return False
                if mapping[last_brace] != brace:
                    return False
        if stack: # Have left braces opened
            return False
        return True
    
inp = '{[]}'
op = Solution().isValid(inp)
print ('Is Valid Pranthesis? = ', op)