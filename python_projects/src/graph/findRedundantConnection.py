'''
Question: The given input is a graph that started as a tree with N nodes (with distinct values 1, 2, ..., N), with one additional edge added. 
The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.

Return an edge that can be removed so that the resulting graph is a tree of N nodes. If there are multiple answers, return the answer 
that occurs last in the given 2D-array. The answer edge [u, v] should be in the same format, with u < v
Input: [[1,2], [2,3], [3,4], [1,4], [1,5]]
Output: [1,4]
Explanation: The given undirected graph will be like this:
5 - 1 - 2
    |   |
    4 - 3
    
Solution: 
    - Keep pruning out the leaves until you are left with a nodes that form a cycle
    - Starting from the last edge, check if both the vertices of the edge are part of the nodes that form the cycle

Created on May 8, 2019

@author: smaiya
'''


from collections import defaultdict
class Solution:
    def findRedundantConnection(self, edges):
        # Form the graph
        graph = defaultdict(set)
        for e in edges:
            graph[e[0]].add(e[1])
            graph[e[1]].add(e[0])
        
        nodes_remaining = set(i for i in graph) # Contains the set of nodes that constitutes the cycle
        leaves = set([i for i in graph if len(graph[i])==1])
        nodes_remaining-=leaves # Remove the leaf nodes from the set
        while leaves:
            next_leaves = set()
            for l in leaves: # Remove each leaf node
                l_conn = graph[l].pop()
                graph[l_conn].remove(l) # Remove the connection from the node the leaf node was connected to
                if len(graph[l_conn])==1:
                    next_leaves.add(l_conn)
            nodes_remaining-=next_leaves
            leaves = next_leaves
        
        # No more leaf nodes in nodes_remaining
        for e in edges[::-1]:
            if e[0] in nodes_remaining and e[1] in nodes_remaining:
                return e