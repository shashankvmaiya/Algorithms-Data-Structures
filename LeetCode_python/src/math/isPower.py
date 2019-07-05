'''
Created on Jul 20, 2018
Given a positive integer which fits in a 32 bit signed integer, 
find if it can be expressed as A^P where P > 1 and A > 0. A and P both should be integers.
@author: smaiya
'''
import math
class Solution:
    # @param A : integer
    # @return an integer
    def isPower(self, A):
        if A == 1:
            return 1
        if A == 2:
            return 0
        for i in range(2, int(math.ceil(math.sqrt(A))+1)):
            Atemp = A
            while Atemp != 1:
                if Atemp%i != 0:
                    break
                Atemp//=i
            if Atemp == 1:
                return 1
        return 0

inp = 2
out = Solution().isPower(inp)
print('Is Power? = ', out)