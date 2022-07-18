'''
295. Find Median from Data Stream

Question: Design a data structure that supports the following two operations:
void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
E.g., 
addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2

Solution: 
    - Maintain 2 heaps: a max_heap and a min_heap
    - max_heap consists of the lower N/2 elements and min_heap consists of the top N/2 elements
    - whenever size of one of the heaps, for example min_heap > size of max_heap +1, then pop the min element from 
    min_heap and push it to the max_heap 
    - median = either min_heap[0] or max_heap[0] or the mean of the two

Created on May 25, 2019

@author: smaiya
'''
import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_heap = []
        self.max_heap = []
        self.size_max, self.size_min = 0, 0

    def addNum(self, num: int):
        if not self.max_heap or num<-self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
            self.size_max+=1
        else:
            heapq.heappush(self.min_heap, num)
            self.size_min+=1            
        if self.size_max-self.size_min>1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
            self.size_max-=1
            self.size_min+=1
        elif self.size_min-self.size_max>1:
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
            self.size_min-=1
            self.size_max+=1

    def findMedian(self):
        if not self.max_heap:
            median = 0
        elif self.size_min==self.size_max:
            median = (self.min_heap[0]-self.max_heap[0])/2
        elif self.size_min<self.size_max:
            median = -self.max_heap[0]
        else:
            median = self.min_heap[0]
        return median


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(2)
param_2 = obj.findMedian()
