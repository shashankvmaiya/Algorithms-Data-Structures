'''
Question: Find the kth largest element in an unsorted array. Note that it is the kth largest element 
in the sorted order, not the kth distinct element.
Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4

Solution: Use min-heap of size k. The top element would be the kth largest

Created on May 12, 2019

@author: smaiya
'''


import heapq
class Solution:
    def findKthLargest(self, nums, k):
        heap = []
        for i, num in enumerate(nums):
            if i<k:
                heapq.heappush(heap, num)
            else:
                heapq.heappushpop(heap, num)
        return heapq.heappop(heap)