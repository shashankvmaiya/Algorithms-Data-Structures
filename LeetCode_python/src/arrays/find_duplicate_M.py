'''
287. Find the Duplicate Number

Question: https://leetcode.com/problems/find-the-duplicate-number/
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. 
Assume that there is only one duplicate number, find the duplicate one.
Input: [1,3,4,2,2]
Output: 2
    - You must not modify the array (assume the array is read only).
    - You must use only constant, O(1) extra space.
    - There is only one duplicate number in the array, but it could be repeated more than once.

Solution: Floyd's Tortoise and Hare (Cycle Detection)
    - Identical to finding entrance of the linked list cycle algorithm
    - First use a slow and a fast pointer to find the intersection location
    - Then find the entrance to the cycle by continuing the slow pointer and using a new pointer which starts from the beginning  

Created on Jun 1, 2019

@author: smaiya
'''

class Solution:
    def findDuplicate(self, nums):
        if not nums:
            return
        slow, fast = nums[0], nums[0]
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break
        
        # Finding the entrance to the cycle
        ptr1, ptr2 = nums[0], slow
        while ptr1!=ptr2:
            ptr1, ptr2 = nums[ptr1], nums[ptr2]
        
        return ptr1
