'''
137. Single Number II

Created on Jul 24, 2018
Given an array of integers, every element appears thrice except for one which occurs once.
Find that element which does not appear thrice.
@author: smaiya
'''


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def mod3bitXor(self, x, y):
        result, bit_pos = 0, 0
        while x!=0 or y!=0:
            x_bit, y_bit = x%3, y%3
            result += (x_bit+y_bit)%3*3**bit_pos
            bit_pos, x, y = bit_pos+1, int(x/3), int(y/3)
        return result
    def singleNumber(self, A):
        #out = 0
        #for num in A:
        #    out = self.mod3bitXor(out, num)
        num_list = dict()
        for num in A:
            num_list[num] = num_list.get(num, 0)+1
            if num_list[num]==3:
                del num_list[num]
        for num in num_list:
            return num

inp = [1, 2, 4, 3, 3, 2, 2, 3, 1, 1]
out = Solution().singleNumber(inp)
print('Single Number which doesnt appear thrice = ', out)