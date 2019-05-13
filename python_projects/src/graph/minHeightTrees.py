'''
Question: For an undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. 
Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to 
find all the MHTs and return a list of their root labels.

Input: n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

     0  1  2
      \ | /
        3
        |
        4
        |
        5 

Output: [3, 4]

Solution: 
    - Every iteration, find the existing leaves from the graph and remove them 
    - The last set of nodes is the result

Created on May 7, 2019

@author: smaiya
'''

class Solution:
    def findMinHeightTrees(self, n, edges):
        if not n: 
            return []
        if n==1:
            return [0]
        if n==2:
            return [0, 1]
        
        # Get degree of each node and graph connections via adjacency list
        degree = [0 for i in range(n)]
        connection = [[] for i in range(n)]
        for e in edges:
            connection[e[0]].append(e[1])
            connection[e[1]].append(e[0])
            degree[e[0]]+=1
            degree[e[1]]+=1
        
        # LEaves = degree of a node = 1
        leaves = [i for i, d in enumerate(degree) if d <=1]
        done = leaves
        next_leaves = []
        while len(done)<n:
            # If there is a cycle, then there are no leaves, but there still will be nodes. 
            if not leaves:
                return list(range(n)).remove(done)
            for l in leaves: 
                for l_conn in connection[l]:
                    if l_conn in done: # All but 1 connection would have already been processed as leaf
                        continue
                    degree[l]-=1
                    degree[l_conn]-=1 
                    if degree[l_conn]==1: # If the connected node ends up with 1 degree, then it is a leaf for next iteration
                        next_leaves.append(l_conn)
            done+=next_leaves
            leaves, next_leaves = next_leaves, []
        return leaves
        
        
