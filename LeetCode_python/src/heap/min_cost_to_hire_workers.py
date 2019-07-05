'''
Question: 
There are N workers.  The i-th worker has a quality[i] and a minimum wage expectation wage[i].

Now we want to hire exactly K workers to form a paid group.  When hiring a group of K workers, 
we must pay them according to the following rules:
    - Every worker in the paid group should be paid in the ratio of their quality compared to other workers in the paid group.
    - Every worker in the paid group must be paid at least their minimum wage expectation.
E.g., 
Input: quality = [3,1,10,10,1], wage = [4,8,2,2,7], K = 3
Output: 30.66667
Explanation: We pay 4 to 0-th worker, 13.33333 to 2-th and 3-th workers seperately. 

Solution: 
    - Every worker has a minium rate = wage/quality. We have to pay max rate among the selected workers
    - Sort based on the rate and start running through the data from the lowest rate 
    - Let's say we hire workers with a ratio R or lower. Then, we would want to know the K workers with 
    the lowest quality, and the sum of that quality. 
    - Use heap to maintain the lowest k-quality workers 

Created on May 25, 2019

@author: smaiya
'''

import heapq
class Solution:
    def mincostToHireWorkers(self, quality, wage, K):
        data = [(w/q, q, w) for (q, w) in zip(quality, wage)]
        data = sorted(data, key=lambda x:x[0]) # Sorted data based on the rate = w/q
        
        max_heap = [] # Stores the lowest K quality
        sum_quality = 0 # Sum of the qualities in the heap
        min_cost = float('Inf')
        # Since we are iterating over data sorted by rate, the rate that we would have to pay for the current
        # chosen worker set will always be the current rate (which is the maximum)
        for rate, q, w in data: 
            if len(max_heap)<K:
                heapq.heappush(max_heap, -q)
                sum_quality+=q
            else:
                highest_q = -heapq.heappushpop(max_heap, -q)
                sum_quality += (q-highest_q)
            if len(max_heap)==K:
                min_cost = min(min_cost, rate*sum_quality)
                
        return min_cost
