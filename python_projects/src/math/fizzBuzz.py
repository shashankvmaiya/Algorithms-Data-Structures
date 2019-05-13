'''
Created on Jul 18, 2018

@author: smaiya
'''

class Solution:
    # @param A : integer
    # @return a list of strings
    def fizzBuzz(self, A):
        out = []
        for i in range(1, A+1):
            if i%15 == 0:
                out.append('FizzBuzz')
            elif i%3 == 0:
                out.append('Fizz')
            elif i%5 == 0:
                out.append('Buzz')
            else:
                out.append(i)
        return out



a = Solution()
n=30
out = a.fizzBuzz(n)
print('out = ', out)
