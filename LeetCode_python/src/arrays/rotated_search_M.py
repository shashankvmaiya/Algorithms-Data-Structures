'''
33. Search in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
You are given a target value to search. If found in the array return its index, otherwise return -1.

Solution: 
    FIrst find the pivot via binary search
    Use the pivot as a fixed starting offset and then do binary search on the offseted array 
Created on Mar 23, 2019

@author: smaiya


'''

class Solution:
    def search(self, nums, target):
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        
        # First find the pivot = min_idx
        left, right = 0, len(nums)-1
        if nums[right]>nums[left]:
            min_idx = left
        else:
            min_idx = int((left+right)/2)
            while nums[right]<nums[left]:
                if min_idx == left:
                    min_idx = right
                    break
                if nums[min_idx]>nums[left]:
                    left=min_idx
                    if nums[left+1]<nums[left]:
                        min_idx = left+1
                        break
                elif nums[min_idx]<nums[right]:
                    right=min_idx
                    if nums[right-1]>nums[right]:
                        min_idx = right
                        break
                min_idx = int((left+right)/2)
            
        offset, n = min_idx, len(nums)
        start, end = (0+offset), (n-1+offset)
        
        if nums[start]==target:
            return start
        if nums[end%n]==target:
            return (end%n)
    
        mid = int((start+end)/2)
        if nums[mid%n]==target:
            return (mid%n) 
        while nums[mid%n]!=target:
            if nums[mid%n]>target:
                end = mid
            elif nums[mid%n]<target:
                start = mid
            mid = int((start+end)/2)
            if nums[mid%n]==target:
                return (mid%n) 
            if mid == start:
                break
        return -1
    
    
inp = [1, 3, 5]
out = Solution().search(inp, 0)
print ('Top k frequent = ', out)
