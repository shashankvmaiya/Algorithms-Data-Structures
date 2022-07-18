'''
162. Find Peak Element

Question: 
A peak element is an element that is greater than its neighbors. Idx 0 and n-1 have just 1 neighbor
Given an input array nums, where nums[i] != nums[i+1], find a peak element and return its index.
The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
You may imagine that nums[-1] = nums[n] = -infty. ==> There definitely is a peak element

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5 
Explanation: Your function can return either index number 1 where the peak element is 2, 
             or index number 5 where the peak element is 6.
             
Solution: Binary Search in O(logn)
    - Go to mid index. If nums[mid] > nums[mid+1], then there is a peak in the left half, hence hi=mid

Created on Apr 7, 2019

@author: smaiya
'''


class Solution:
    def findPeakElement(self, nums):
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + hi >> 1
            if nums[mid] > nums[mid+1]: hi = mid
            else: lo = mid + 1
        return lo
    