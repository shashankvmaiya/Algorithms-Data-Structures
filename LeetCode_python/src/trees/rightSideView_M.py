'''
199. Binary Tree Right Side View

Question: Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
  
Solution: DFS Approach
        - Preorder traversal with right child processed first
        - In right child first pre-order traversal, the first child processed at each level is always the right most node
    BFS Approach
        - Do BFS by adding the right child first and then the left child into the queue
        - Each level, store the first  node value into the result array
Created on May 12, 2019

@author: smaiya
'''

# Definition for a  binary tree node
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
        

class Solution:
    def rightSideView(self, root):
        result = []
        level = 0
        self.dfs(root, result, level)
        return result
    
    def dfs(self, node, result, level):
        if not node:
            return
        if len(result)==level: # If the first node for this level, then append it to the result array
            result.append(node.val)
        
        if node.right:
            self.dfs(node.right, result, level+1)
        if node.left:
            self.dfs(node.left, result, level+1)
