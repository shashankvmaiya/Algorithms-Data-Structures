'''
841. Keys and Rooms

Question: 
There are N rooms and you start in room 0.  Each room has a distinct number in 0, 1, 2, ..., N-1, and each room may have some keys to access the next room. 

Formally, each room i has a list of keys rooms[i], and each key rooms[i][j] is an integer in [0, 1, ..., N-1] where N = rooms.length.  
A key rooms[i][j] = v opens the room with number v.
Initially, all the rooms start locked (except for room 0). 
You can walk back and forth between rooms freely.
Return true if and only if you can enter every room.

Solution: 
    - Use Breadth first search and maintain a visited list  

Created on May 8, 2019

@author: smaiya
'''

from collections import defaultdict
from functools import reduce
class Solution:
    def canVisitAllRooms(self, rooms):
        graph = defaultdict(list)
        for idx, r in enumerate(rooms):
            for k in r:
                graph[idx].append(k)
                
        visited = [False for i in range(len(rooms))]
        queue = [0]
        while queue:
            r = queue.pop(0)
            visited[r] = True
            for r_conn in graph[r]:
                if not visited[r_conn]:
                    queue.append(r_conn)
                    
        all_rooms = reduce(lambda x, y: x and y, visited)
        return all_rooms

