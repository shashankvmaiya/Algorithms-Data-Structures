'''
75. Sort Colors

Question: 
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the 
same color are adjacent, with the colors in the order red, white and blue.
Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Come up with a one pass algorithm using constant space

Solution:
    - Two pass Solution 
        - count the number of 0s and 1s. Overwrite the list with the total number of 0s, 1s and 2s
    - One pass solution: 
        - Maintain left and right pointer which indicates the first position which is not a 0 and 2 
        - If current index element is 0, then swap that with the element in left pointer (which contains 1) and left+=1
        - If current index element is 2, then swap that with the element in right pointer (which has not yet been explored)
        and right-=1, ctr-=1
        - Else (element =1) just ctr+=1 

Created on Apr 6, 2019

@author: smaiya
'''
class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums)-1
        ctr = 0
        while ctr<=right:
            if nums[ctr]==0:
                nums[left], nums[ctr] = nums[ctr], nums[left]
                left+=1
            elif nums[ctr]==2:
                nums[right], nums[ctr] = nums[ctr], nums[right]
                right-=1
                ctr-=1
            ctr+=1
