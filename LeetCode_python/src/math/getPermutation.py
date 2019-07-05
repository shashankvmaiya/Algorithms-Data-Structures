'''
Question: Given n and k, return the kth permutation sequence.
The set [1,2,3,...,n] contains a total of n! unique permutations.
By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
Input: n = 3, k = 3
Output: "213"

Solution: Quotient Remainder approach. 
    - Divide k by (n-1)! Quotient corresponds to the index of the first number in the permutation sequence
    - Divide the remainder by (n-2)! This quotient will correspond to the second number in the remaining numbers

Created on Apr 5, 2019

@author: smaiya
'''
import math
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = list(range(1, n+1))
        k-=1
        permutation = ''
        for i in range(n):
            quotient, k = divmod(k, math.factorial(n-i-1))
            permutation+=str(nums[quotient])
            nums.pop(quotient)
        return permutation
    