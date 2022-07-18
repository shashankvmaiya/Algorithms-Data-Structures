'''
Question: Given a n x n matrix where each of the rows and columns are sorted in ascending order, 
find the kth smallest element in the matrix.
E.g.
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,
return 13.

Solution: 
    - Maintain a max_heap of size k
    - Few run time optimizations since matrix is sorted row and column wise
        - while scanning columns of a row, if a element > max_heap[0], then break 
        - while scanning rows, if the first element > max_heap[0], then stop scanning remaining rows

Created on May 25, 2019

@author: smaiya
'''

import heapq
class Solution:
    def kthSmallest(self, matrix, k):
        max_heap, ctr = [], 0
        for row in matrix:
            # If first element of row is > max_heap[0], all the rows following will have elements > max_heap[0]
            if ctr>=k and row[0]>=-max_heap[0]: 
                break
            for num in row:
                if ctr<k:
                    heapq.heappush(max_heap, -num)
                    ctr+=1
                elif num<-max_heap[0]:
                    heapq.heappushpop(max_heap, -num)
                else: # If num>max_heap[0], then all the elements following it is > max_heap[0]
                    break
        return -max_heap[0]
