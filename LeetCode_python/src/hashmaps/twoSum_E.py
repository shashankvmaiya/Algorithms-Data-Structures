'''
1. Two Sum
Given an array of integers nums and an integer target, return indices of the two 
numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use 
the same element twice.

You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

'''
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def twoSum(self, A, B):
        n = len(A)
        remainder = dict()
        for i in range(n):
            num = A[i]
            if num in remainder:
                index2 = i+1
                index1 = remainder[num]
                return [index1, index2]
            else:
                remainder[B-num] = remainder.get(B-num, i+1)
        return []

a = Solution()
inp = [2, 3, 11, 15, 3]
inp2 = 6
str = a.twoSum(inp, inp2)
print ('Two Sum = ', str)
