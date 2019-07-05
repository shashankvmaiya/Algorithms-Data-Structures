'''
Question: We have a list of points on the plane.  Find the K closest points to the origin (0, 0).
(Here, the distance between two points on a plane is the Euclidean distance.)
Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)

Solution: 
    - Maintain a max_heap: which consists of the K closest points to the origin
    - If the new point is closer (lower) than the maximum of those K points, add that point and pop the max point

Created on May 25, 2019

@author: smaiya
'''

import heapq
class Solution:
    def kClosest(self, points, K):
        max_heap = []
        for idx, p in enumerate(points):
            distance = p[0]**2+p[1]**2
            if idx<K:
                heapq.heappush(max_heap, (-distance, p))
            elif distance<-max_heap[0][0]:
                heapq.heappushpop(max_heap, (-distance, p))
        return [x[1] for x in max_heap]
    