'''
Created on Jul 1, 2018
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
@author: smaiya
'''

class MinStack:
    stack, min_stack = list(), list()
    def __init__(self):
        while self.stack:
            self.stack.pop()
        while self.min_stack:
            self.min_stack.pop()
    # @param x, an integer
    def push(self, x):
        self.stack.append(x)
        min_element = x if self.min_stack == [] or x<self.min_stack[-1] else self.min_stack[-1]
        self.min_stack.append(min_element)

    # @return nothing
    def pop(self):
        if self.stack:
            self.min_stack.pop()
            return self.stack.pop()
        else:
            return None


    # @return an integer
    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            return -1


    # @return an integer
    def getMin(self):
        if self.min_stack:
            return self.min_stack[-1]
        else:
            return -1


a = MinStack()
print(a.getMin())
print(a.top())
print(a.top())
a.push(10)
a.push(8)
a.push(6)
print(a.pop())
print(a.top())
print(a.getMin())
a.push(5)
print(a.top())
print(a.getMin())
a.pop()
a.pop()
a.pop()
print(a.getMin())
print(a.top())
print(a.pop())


