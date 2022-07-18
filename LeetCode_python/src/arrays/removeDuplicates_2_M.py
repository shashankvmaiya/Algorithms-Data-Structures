'''
80. Remove Duplicates from Sorted Array II

Question: Given a sorted array nums, remove the duplicates in-place such that duplicates appeared 
at most twice and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place 
with O(1) extra memory.

Given nums = [0,0,1,1,1,1,2,3,3],
Your function should return length = 7, with the first seven elements of nums being modified 
to 0, 0, 1, 1, 2, 3 and 3 respectively.

Solution: 
    - Maintain a pointer indicating the next location of new element
    - If nums[i] != nums[idx-2], then the number hasnt yet appeared > 2 times. Hence copy that element to idx and idx+=1

Created on Apr 6, 2019

@author: smaiya
'''

class Solution:
    def removeDuplicates(self, nums):
        if len(nums)<=2:
            return len(nums)
        idx = 2
        for i in range(2, len(nums)):
            if nums[i]!=nums[idx-2]:
                nums[idx] = nums[i]
                idx+=1
        return idx

