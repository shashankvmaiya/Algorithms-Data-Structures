'''
98. Validate Binary Search Tree

Question: Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:
    - The left subtree of a node contains only nodes with keys less than the node's key.
    - The right subtree of a node contains only nodes with keys greater than the node's key.
    - Both the left and right subtrees must also be binary search trees.

Solution: In order traversal. Check if the values are >= the previous value

Created on Apr 3, 2019
@author: smaiya
'''

# Definition for a  binary tree node
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def isValidBST(self, root):
        if not root:
            return True
        stack = []
        node = root
        value = -float('inf')
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                curr_node = stack.pop()
                if value>=curr_node.val:
                    return False
                value = curr_node.val
                node = curr_node.right
        return True