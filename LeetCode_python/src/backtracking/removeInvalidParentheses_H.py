
'''
301. Remove Invalid Parentheses

Given a string s that contains parentheses and letters, remove the minimum number of 
invalid parentheses to make the input string valid.

Return all the possible results. You may return the answer in any order.
Input: s = "()())()"
Output: ["(())()","()()()"]

Input: s = "(a)())()"
Output: ["(a())()","(a)()()"]

Input: s = ")("
Output: [""]

Solution
    - Starting from the original string s, check if it is valid or not
    - If not valid, obtain a set of all strings by removing a character from previous candidate set
    - Check if any of the possible string in the candidate set is valid or not

Created on July 18, 2022
@author: smaiya
'''

from typing import Dict, Any, List
from collections import defaultdict


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        candidates = {s}
        while True:
            result = list(filter(self.isValid, candidates))
            if result:
                return result
            # update candidates with all possible strings with 1 additional character removed
            candidates = {st[:i] + st[i+1:] for st in candidates for i in range(len(st))}

    # check if valid
    def isValid(self, s):
        ctr = 0
        for c in s:
            if c == '(':
                ctr+=1
            elif c == ')':
                ctr-=1
                if ctr<0:
                    return False
        if ctr==0:
            return True
        return False

s = "()())()"
ans = Solution().removeInvalidParentheses(s)
