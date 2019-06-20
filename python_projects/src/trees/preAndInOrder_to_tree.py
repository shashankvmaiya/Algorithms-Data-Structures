'''
Question: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
Given preorder and inorder traversal of a tree, construct the binary tree.
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
    3
   / \
  9  20
    /  \
   15   7
   
Solution: 
    - When we take an item from preorder list, we can use the inorder list to find its left and right subtrees
        - preorder: root>left subtree>right subtree and inorder: left subtree>root>right subtree
    - Look for the idx or preorder in inorder
        - All items from start to idx-1 would belong to the left subtree 
        - All items from idx+1 to end would belong to the right subtree 

Created on Jun 1, 2019

@author: smaiya
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        self.pre_idx = 0
        self.inorder_dict = {v:k for k, v in enumerate(inorder)} # Use dictionary for faster look up of inorder idx
        return self.build(preorder, 0, len(inorder)-1)
        
    def build(self, preorder, low, high):
        if high<low or self.pre_idx==len(preorder):
            return
        node = TreeNode(preorder[self.pre_idx])
        self.pre_idx+=1
        inorder_idx = self.inorder_dict[node.val]
        node.left = self.build(preorder, low, inorder_idx-1)
        node.right = self.build(preorder, inorder_idx+1, high)
        return node
    
    
    