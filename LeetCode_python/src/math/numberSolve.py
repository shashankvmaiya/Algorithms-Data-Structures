'''
Created on Jul 22, 2018

@author: smaiya
'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def num_less(self, array, inp_num):
        out = 0
        for num in array:
            if num<inp_num:
                out+=1
        return out
    
    def solve(self, A, B, C):
        n = len(A)
        zero_present = 0 in A
        
        out = 0
        C_str = str(C)
        num_digits = len(C_str)
        if num_digits < B:
            return 0
        if num_digits > B:
            out = (n-1)*n**(B-1) if zero_present and B>1 else n**B
            return out
        for i in range(num_digits):
            digit = int(C_str[i])
            num_less_digit = self.num_less(A, digit)
            out = out+(num_less_digit-1)*n**(num_digits-i-1) if i==0 and zero_present and num_digits>1 else (out+num_less_digit*n**(num_digits-i-1))
            if digit not in A:
                break
        return out


inp, n, k = [0, 1, 5], 1, 2
inp, n, k = [0, 1, 2, 5], 2, 21
inp, n, k = [0, 2, 3, 4, 5, 7, 8, 9], 5, 86587
inp, n, k = [2, 3, 4, 5, 7, 8, 9], 5, 8658
inp, n, k = [0, 4, 5, 7, 8], 1, 51782
inp, n, k = [0, 4, 5, 7, 8], 2, 51782
inp, n, k = [4, 5, 7, 8], 2, 51782
out = Solution().solve(inp, n, k)
print('Number of numbers of length N and value less than K = ', out)
