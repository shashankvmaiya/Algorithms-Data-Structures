'''
303. Range Sum Query - Immutable

Question: Given an integer array nums, find the sum of the elements between indices i and j (i <= j), inclusive.
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3

Solution: 
    - Store a sum array which stores sum from 0 to i
    - sumRange[i:j] = sum[j+1] - sum[i]

Created on May 31, 2019

@author: smaiya
'''

class NumArray:

    def __init__(self, nums):
        if nums:
            self.sum = [0]
            for num in nums:
                self.sum.append(num+self.sum[-1])

    def sumRange(self, i: int, j: int) -> int:
        return self.sum[j+1]-self.sum[i]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)