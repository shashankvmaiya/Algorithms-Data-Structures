'''
Question: Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days 
you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

Solution: Use stacks
    - Initialize output to all 0
    - stack contains indices of all days where higher temperature is not found
        - Hence the stack will contain indices pointing to temperatures in descending order
    - The moment a higher temperature is found, pop from stack and update all the cooler days with this temperature   

Created on Apr 21, 2019

@author: smaiya
'''


class Solution:
    def dailyTemperatures(self, T):
        n = len(T)
        out = [0 for i in range(n)]
        
        stack = []
        for i, temp in enumerate(T):
            # Check if current temperature is higher than the temperatures in the stack
            while stack and T[stack[-1]]<temp:
                idx = stack.pop()
                out[idx] = i-idx
            stack.append(i)
        return out
    
    