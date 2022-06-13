'''
There is a binary tree rooted at 0 consisting of n nodes. The nodes are labeled from 0 to n - 1. 
You are given a 0-indexed integer array parents representing the tree, where parents[i] 
is the parent of node i. Since node 0 is the root, parents[0] == -1.

Each node has a score. To find the score of a node, consider if the node and the edges 
connected to it were removed. The tree would become one or more non-empty subtrees. 
The size of a subtree is the number of the nodes in it. The score of the node is the 
product of the sizes of all those subtrees.

Return the number of nodes that have the highest score.

Input: parents = [-1,2,0,2,0]
     0
    / \
   2   4
  / \
 3   1

Output: 3
Explanation:
- The score of node 0 is: 3 * 1 = 3
- The score of node 1 is: 4 = 4
- The score of node 2 is: 1 * 1 * 2 = 2
- The score of node 3 is: 4 = 4
- The score of node 4 is: 4 = 4
The highest score is 4, and three nodes (node 1, node 3, and node 4) have the highest score.

Solution:
    - Post order traversal since child nodes are processed before parent nodes
    - dfs returns the number of nodes in the subtree
    - if node is leaf node, then score = total number of nodes in the tree - 1
    - if node is root, then score = num nodes in left tree * num nodes in right tree
    - for any other node, score = num nodes in left tree * num nodes in right tree * num rest of the nodes - 1

Created on June 11, 2022
@author: smaiya
'''

import math
class Solution:
    def countHighestScoreNodes(self, parents):
        self.max_score = 0
        self.count = 0
        self.children = {}
        self.n = len(parents)
        for i, p in enumerate(parents):
            if p>=0:
                if p in self.children:
                    self.children[p].append(i)
                else:
                    self.children[p] = [i]
        
        self.dfs(0)
        return self.count
        
    def dfs(self, node):
        children = self.children[node] if node in self.children else []
        subtree_size = []
        for c in children:
            n = self.dfs(c)
            subtree_size.append(n)
        if children:
            rest_size = self.n - sum(subtree_size) - 1
            subtree_prod = math.prod(subtree_size)
            score = subtree_prod if node==0 else rest_size * subtree_prod
        else:
            score = self.n-1
        if score > self.max_score:
            self.max_score, self.count = score, 1
        elif score==self.max_score:
            self.count+=1
        return sum(subtree_size)+1

parents = [-1,2,0,2,0]
ans = Solution().countHighestScoreNodes(parents)
print('Count highest score nodes = ', ans)

