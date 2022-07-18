'''
227. Basic Calculator II

Question: Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . 
The integer division should truncate toward zero.
Input: " 3+5 / 2 "
Output: 5

Input: '3+4*2/3'
Output: 5

Solution: Use Stack. 2 pass solution
    - Process only the * and / in the first pass and store them in stack (store +num if + is used and -num if - is used)
    - The result = sum of the numbers in stack 

Created on May 31, 2019

@author: smaiya
'''

class Solution:
    def calculate(self, s):
        
        stack = []
        num = 0
        prev_sign = '+'
        for i, c in enumerate(s):
            if c.isdigit():
                num = num*10 + int(c)
                
            if c in '+-*/' or i==len(s)-1:
                if prev_sign == '+':
                    stack.append(num)
                elif prev_sign == '-':
                    stack.append(-num)
                elif prev_sign == '*':
                    prev_num = stack.pop()
                    stack.append(prev_num*num)
                elif prev_sign == '/':
                    prev_num = stack.pop()
                    stack.append(int(prev_num/num))
                prev_sign = c
                num = 0
        return sum(stack)
