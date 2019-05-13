'''
Question: Given a binary tree, find the leftmost value in the last row of the tree.

Solution: Identical Approach to rightSideView. Here, we just return the last element in the 'left' side view result 
    - DFS Approach
        - Preorder traversal with left child processed first
        - In left child first pre-order traversal, the first child processed at each level is always the left most node
    BFS Approach
        - Do BFS by adding the left child first 
        - Each level, store the first  node value into the result array
        - Output the last element of the result array

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
    def findBottomLeftValue(self, root):
        
        def dfs(node, result, level):
            if not node:
                return
            if len(result)==level: # If the first node for this level, then append it to the result array
                result.append(node.val)
                
            if node.left:
                dfs(node.left, result, level+1)
            if node.right:
                dfs(node.right, result, level+1)
        
        result=[]
        dfs(root, result, 0)
        return result[-1]