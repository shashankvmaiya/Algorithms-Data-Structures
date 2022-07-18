'''
41. First Missing Positive

Question: Given an unsorted integer array, find the smallest missing positive integer.
Input: [3,4,-1,1]
Output: 2

Input: [1,2,0]
Output: 3

Solution: 
    - For any array whole length is n, the first missing positive must be in the range [1 to n+1]
    - Map all elements outside the range (<0 and >=n) to 0. (n and n+1 are handled separately)
    - Use array index as the hash, increment the index of every number by n
    - Starting from the smallest index, check if each number > n. If not, then that number is absent 
    
Created on Apr 5, 2019

@author: smaiya
'''

class Solution:
    def firstMissingPositive(self, nums):
        if not nums:
            return 1
        n = len(nums)
        n_present = False
        # Map all numbers outside the range to 0. 
        for i in range(n):
            if nums[i]==n:
                n_present=True
            if nums[i]<0 or nums[i]>=n:
                nums[i]=0
        # Using index as hash. Increment the index of every number by n
        for i in range(n):
            if nums[i]%n>0:
                nums[nums[i]%n]+=n
                
        # Starting from the smallest index, check if each number > n. If not, then that number is absent 
        for i in range(1, n):
            if nums[i]//n==0:
                return i
        # All numbers from 1 to n-1 are present
        if n_present:
            return n+1
        else:
            return n


inp = [1, 2, 0]
inp = [1, 2, 3]
op = Solution().firstMissingPositive(inp)
print ('First Missing Positive Number = ', op)