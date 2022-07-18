'''
239. Sliding Window Maximum

Question: 
Given an array nums, there is a sliding window of size k which is moving from the very left of the 
array to the very right. You can only see the k numbers in the window. Each time the sliding window moves 
right by one position. Return the max sliding window.
Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 

Solution: 
    - Use max heap
        - Push the number and index into the heap
        - Check if the index of the top element is within the sliding window
        - If not, then pop the element and check the next  
Created on May 13, 2019

@author: smaiya
'''

import heapq
class Solution:
    def maxSlidingWindow(self, nums, k):
        heap = []
        curr_max, idx = float('-Inf'), -1
        max_array = []
        for i, num in enumerate(nums):
            heapq.heappush(heap, (-num, i))
            if i>=k-1:
                while heap[0][1]<i-k+1:
                    heapq.heappop(heap)
                curr_max, idx = -heap[0][0], heap[0][1]
                max_array.append(curr_max)
        return max_array