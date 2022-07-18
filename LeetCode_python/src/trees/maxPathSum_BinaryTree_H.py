'''
124. Binary Tree Maximum Path Sum

Question: Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. 
The path must contain at least one node and does not need to go through the root.
Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42

Solution: Post order traversal - process child nodes before parent node
    - Get the node_max for the child nodes
    - node_max for the parent node = max(parent_value, node_max of left child node + parent_value, node_max of right child node + parent_value)
    - Maintain a global max_sum, which also performs max over parent_value + node_max of left child node + node_max of right child node

Created on Apr 21, 2019

@author: smaiya
'''

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def maxPathSum(self, root):
        if root is None:
            return None
        if root.left is None and root.right is None:
            return root.val
        self.max_sum = float('-inf')
        self.dfs(root)
        return self.max_sum
    
    def dfs(self, node):
        if node is None:
            return float('-inf')
        
        left_max = self.dfs(node.left)
        right_max = self.dfs(node.right)
        
        curr_val = node.val
        node_max = max(curr_val, curr_val+left_max, curr_val+right_max)
        self.max_sum = max(self.max_sum, node_max, curr_val+left_max+right_max)
        return node_max
    
    