'''
611. Valid Triangle Number

Question: Given an array consists of non-negative integers, your task is to count the number 
of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.
Input: [2,2,3,4]
Output: 3
Explanation:
Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3


Solution: 
    - Sort the array
    - i in range(0, n-2), move j and k together. O(n^2)
        - k starts from i+2
        - j in range(i+1, n-2)
    - For each j, increment k till num[i]+num[j]<num[k] and store the number of triangles for (i, j) combination
    
Created on Apr 7, 2019

@author: smaiya
'''

class Solution:
    def triangleNumber(self, nums):
        if len(nums)<3:
            return 0
        nums.sort()
        count = 0
        for i in range(0, len(nums)-2):
            if nums[i] == 0:
                continue
            k = i+2
            for j in range(i+1, len(nums)-1):
                while k<len(nums) and nums[i]+nums[j]>nums[k]:
                    k+=1
                count+=(k-j-1)
                
        return count

