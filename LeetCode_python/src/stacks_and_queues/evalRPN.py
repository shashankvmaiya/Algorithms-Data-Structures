'''
Created on Jun 30, 2018
Evaluate the value of an arithmetic expression in Reverse Polish Notation.
 ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
 ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
@author: smaiya
'''

class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        inp_data = list()
        for data in A:
            if data in ("+", "-", "*", "/"):
                num2 = inp_data.pop()
                num1 = inp_data.pop()
                if data == "+":
                    inp_data.append(num1+num2)
                elif data == "-":
                    inp_data.append(num1-num2)
                elif data == "*":
                    inp_data.append(num1*num2)
                elif data == "/":
                    inp_data.append(int(num1/num2))
            else:
                inp_data.append(int(data))
        return inp_data.pop()
                
            


a = Solution()
inp = ["2", "1", "+", "3", "*"]
inp = ["4", "13", "5", "/", "+"]
out = a.evalRPN(inp)
print ('Result = ', out)
