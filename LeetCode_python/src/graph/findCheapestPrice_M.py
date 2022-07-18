'''
Question: There are n cities connected by m flights. Each fight starts from city u and arrives at v with a price w.

Now given all the cities and flights, together with starting city src and the destination dst, your task is to find the cheapest price 
from src to dst with up to k stops. If there is no such route, output -1.

Solution: Use Dijkstras algorithm with a modification. Visit the node again, provided it has <= stops
    - Each node has to be relaxed though it was relaxed earlier, since we are trying to find the 
    cheapest path up to k-stops. The earlier relaxed instance might be with higher number of stops

Created on May 12, 2019

@author: smaiya
'''

import heapq
import collections
class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        graph = collections.defaultdict(list)
        for f in flights:
            graph[f[0]].append([f[1], f[2]])
        
        pq = [(0, src, 0)] # (cost, node, stop_idx)
        while pq:
            cost, node, stop_idx = heapq.heappop(pq)
            # We are only relaxing the node, if stop_idx<=k. Hence, stop_idx is guaranteed to be <=K+1
            # The first popped out node which is destination is the one with the lowest cost
            if node==dst: 
                return cost
            if stop_idx<=K: # Do not relax/extend if > K stops
                for dest in graph[node]:
                    heapq.heappush(pq, (cost+dest[1], dest[0], stop_idx+1))
        return -1