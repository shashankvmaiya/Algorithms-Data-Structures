'''
279. Perfect Squares

Question: Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.

Solution: Use Breadth First Search
    - Optimizations: Maintain a set of sum of squares to prevent including multiple copies of the same sum

Created on May 12, 2019

@author: smaiya
'''


class Solution:
    def numSquares(self, n):
        squares = [i**2 for i in range(1, int(n**0.5 + 1))]
        
        count, queue, next_queue = 0, set(), set()
        queue.add(0)
        while queue:
            for curr_sum in queue:
                for sq in squares:
                    if curr_sum+sq==n:
                        return count+1
                    elif curr_sum+sq<n:
                        next_queue.add(curr_sum+sq)
                    else:
                        break
            count, queue, next_queue = count+1, next_queue, set()