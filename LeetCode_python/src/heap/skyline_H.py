'''
218. The Skyline Problem

Question: https://leetcode.com/problems/the-skyline-problem/
A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. 
Now suppose you are given the locations and height of all the buildings as shown on a cityscape photo (Figure A), 
write a program to output the skyline formed by these buildings collectively (Figure B).

The geometric information of each building is represented by a triplet of integers [Li, Ri, Hi], where Li and Ri are 
the x coordinates of the left and right edge of the ith building, respectively, and Hi is its height. 
It is guaranteed that 0 <= Li, Ri <= INT_MAX, 0 < Hi <= INT_MAX, and Ri - Li > 0. 
You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

Solution: 
    - Sort the array by start point (use a flag (k) to indicate if it is the building start or end)
    - Use heap to keep the heights of the building that have started and not yet ended
    - If k=0 (building start), if current building height > max in heap, then add to result. Add the height to heap
    - If k=1 (building end), remove height from heap. If building height > max in heap, then add the max in heap to the result 
Below solution not fully optimized since removing height from heap uses O(N). 
It can be further optimized to use O(log N) using heap 

Created on Jun 1, 2019

@author: smaiya
'''

import heapq
class Solution:
    def getSkyline(self, buildings):
        max_heap = [0]
        res = []
        # xy stores the x, y co-ordinate of the building. The third dimension = 0 if building start 1 if building end
        # If a building ends and starts at the same x-coordinate, process the start first
        # Hence, sort xy based on x co-ordinate, followed by start/end and then the y coordinate
        xy = [i for l, r, h in buildings for i in [[l, h, 0], [r, h, 1]]]
        xy = sorted(xy, key=lambda x:(x[0], x[2], x[1]))
        
        for x, y, k in xy:
            if k==0: # If building start
                if y>-max_heap[0]: # If new building start has higher y than all the existing buildings 
                    # If there was another building with same x, then use the one with higher y (which is the latest one) 
                    if res and x==res[-1][0]: 
                        res.pop()
                    res.append([x, y])
                heapq.heappush(max_heap, -y) # Push the new building into the heap
            else: # If building end
                max_heap.remove(-y) # Pop the building from the heap. Can be further optimized to run in O(N)
                heapq.heapify(max_heap) # Heapify again since popping will remove heap invariance 
                if y>-max_heap[0]: # If building that is removed had higher y than all the existing buildings 
                    # Among all buildings with same x, the building with largest y will be processed at the end 
                    # Hence the additional check not required
                    res.append([x, -max_heap[0]])
        return res
