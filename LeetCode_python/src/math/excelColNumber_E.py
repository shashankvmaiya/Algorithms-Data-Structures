'''
171. Excel Sheet Column Number

Given a string columnTitle that represents the column title as appears in an Excel sheet, 
return its corresponding column number.
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...

Input: columnTitle = "AB"
Output: 28

Created on Jul 18, 2018
@author: smaiya
'''

class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        out = 0
        Atemp = A[::-1]
        for i in range(len(A)):
            char = Atemp[i]
            out += (ord(char.upper())-64) * 26**i
        return out
            


a = Solution()
inp = 'AB'
out = a.titleToNumber(inp)
print('out = ', out)