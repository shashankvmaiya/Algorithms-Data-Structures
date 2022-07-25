'''
797. All Paths From Source to Target

Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, 
find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit 
from node i (i.e., there is a directed edge from node i to node graph[i][j]).

Input: graph = [[1,2],[3],[3],[]]
0 -> 1
|    |
v    v
2 -> 3

Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

Solution
    - Using dfs, search through each path not visiting the same node again
    - Add the path to result if node visited is n-1

Created on July 19, 2022
@author: smaiya
'''
from typing import Dict, Any, List
from collections import defaultdict


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.result = []
        self.n = len(graph)
        self.dfs(graph, 0, set([0]), [0])
        return self.result
    
    def dfs(self, graph, idx, visited, path):
        if idx==self.n-1:
            self.result.append(path.copy())
            return
        
        for n in graph[idx]:
            if n not in visited:
                visited.add(n)
                self.dfs(graph, n, visited, path+[n])
                visited.remove(n)

