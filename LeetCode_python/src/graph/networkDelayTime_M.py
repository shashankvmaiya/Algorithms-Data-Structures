'''
743. Network Delay Time

Question: 
There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, 
v is the target node, and w is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.

Solution: Use Dijkstra Algorithm with Heap (min heap)
    - Maintain visited node list and the corresponding time to travel to that node
    - Pop the node with the smallest time (top node of the heap) and extend it to all its neighbors and add those to the heap 

Created on May 8, 2019

@author: smaiya
'''

from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times, N, K):
        network = defaultdict(list)
        for t in times:
            network[t[0]].append([t[1], t[2]])
        
        heap = [(0, K)]
        visited = {}
        while heap:
            t, node = heapq.heappop(heap) # Pop the node at the top of the heap with minimum travel time
            if node not in visited:
                visited[node] = t
                for dest in network[node]:
                    heapq.heappush(heap, (t+dest[1], dest[0])) # Add all values into the heap. Only the node with minimum time will be considered  
        
        return max(visited.values()) if len(visited)==N else -1
        
