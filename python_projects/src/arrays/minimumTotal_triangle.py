'''
Question: Given a triangle, find the minimum path sum from top to bottom. 
Each step you may move to adjacent numbers on the row below.
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Solution: Dynamic Programming
    - D(n) = Minimum total for each element up to nth row
    - D(n+1, i) = triangle(n+1, i) + min(D(n, i-1), D(n, i))
    - Update from the last element to avoid overwriting

Created on Apr 7, 2019

@author: smaiya
'''

class Solution:
    def minimumTotal(self, triangle):
        if not triangle: 
            return 0
        if len(triangle)==1:
            return triangle[0][0]
        
        min_total = [0 for i in range(len(triangle))]
        min_total[0] = triangle[0][0]
        for row_idx in range(1, len(triangle)):
            min_total[row_idx] = min_total[row_idx-1] + triangle[row_idx][row_idx]
            for col_idx in range(row_idx-1, 0, -1):
                min_total[col_idx] = triangle[row_idx][col_idx] + min(min_total[col_idx], min_total[col_idx-1])
            min_total[0] += triangle[row_idx][0]
            
        return min(min_total)

