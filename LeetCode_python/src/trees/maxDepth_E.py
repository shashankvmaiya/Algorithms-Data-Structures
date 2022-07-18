'''
104. Maximum Depth of Binary Tree

Created on Jul 3, 2018
Given a binary tree, find its maximum depth.
The maximum depth of a binary tree is the number of nodes along the longest path from the 
root node down to the farthest leaf node.

Solution: Use any tree traversal. Store the depth of each node and return the max
    - Below, we use preorder traversal. 
@author: smaiya
'''

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    # @param A : root node of tree
    # @return an integer
    
    def maxDepth(self, root):
        if root is None:
            return 0
        self.max_depth = 1
        self.preorder(root, 1)
        return self.max_depth
    
    def preorder(self, root, depth):
        if not root:
            return None
        self.max_depth = max(depth, self.max_depth)
        self.preorder(root.left, depth+1)
        self.preorder(root.right, depth+1)
    
    def maxDepth2(self, A):
        if A is None:
            return 0
        stack = [A]
        depth = [1]
        max_depth = 0
        while stack:
            curr_node = stack.pop()
            curr_depth = depth.pop()
            if curr_node.right:
                stack.append(curr_node.right)
                depth.append(curr_depth+1)
            if curr_node.left:
                stack.append(curr_node.left)
                depth.append(curr_depth+1)
            if curr_node.left is None and curr_node.right is None:
                max_depth = max(max_depth, curr_depth)
        return max_depth


a = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

out = a.maxDepth(root)
print('Max Depth = ', out)
