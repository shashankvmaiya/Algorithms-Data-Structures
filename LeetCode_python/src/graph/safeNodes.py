'''
Question: In a directed graph, we start at some node and every turn, walk along a directed edge of the graph.  
If we reach a node that is terminal (that is, it has no outgoing directed edges), we stop.
Now, say our starting node is eventually safe if and only if we must eventually walk to a terminal node.
 
In a graph, all nodes that are not part of a cycle are safe states.

Example:
Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]

Solution: Use DFS
    - Have to run DFS separately on each node since the graph can be disconnected
    - WHITE, GRAY and BLACK states used
    - Initialized to WHITE
    - First time we visit the node, mark it GRAY
    - If we visit it again during the same DFS, then cycle is found
    - If no cycle, then mark the node as BLACK/safe node

Created on May 11, 2019

@author: smaiya
'''


class Solution:
    def eventualSafeNodes(self, graph):
        WHITE, GRAY, BLACK = 0, 1, 2
        n = len(graph)
        color = [WHITE for _ in range(n)]
        safe = [True for _ in range(n)]
        for i in range(n):
            self.dfs(i, graph, color, safe)
        return [i for i, t in enumerate(safe) if t]
        
    def dfs(self, node, graph, color, safe):
        WHITE, GRAY, BLACK = 0, 1, 2
        if color[node] != WHITE: # If not entering for the first time
            safe[node] = (color[node] == BLACK)
            return
        
        color[node] = GRAY # Mark the node GRAY on entry
        for n in graph[node]:
            if color[n] == BLACK:
                continue
            if color[n] == GRAY:
                safe[node], safe[n] = False, False
                return
            self.dfs(n, graph, color, safe)
            if not safe[n]:
                safe[node] = False
                return
            
        color[node] = BLACK
        safe[node] = True
        return
        