'''
Created on Jul 8, 2018
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses of length 2*n.

For example, given n = 3, a solution set is:
"((()))", "(()())", "(())()", "()(())", "()()()"

@author: smaiya
'''

class Solution:
    # @param A : integer
    # @return a list of strings
    def gen_paranthesis(self, result, buffer, n, open, close):
        if open<n:
            self.gen_paranthesis(result, buffer+'(', n, open+1, close)
        if close<open:
            self.gen_paranthesis(result, buffer+')', n, open, close+1)
        if len(buffer) == 2*n:
            result.append(buffer)
        return result
        
        
    def generateParenthesis(self, A):
        result = self.gen_paranthesis([], '', A, 0, 0)
        return result



a = Solution()
n=3
out = a.generateParenthesis(n)
print('Parenthesis Combinations = ', out)

