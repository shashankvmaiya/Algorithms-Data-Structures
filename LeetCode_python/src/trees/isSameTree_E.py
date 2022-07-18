'''
Created on Jul 3, 2018
Given two binary trees, write a function to check if they are equal or not.
Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
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
    # @param B : root node of tree
    # @return an integer
    def isSameTree(self, A, B):
        if A is None and B is None:
            return 1
        if A is None or B is None:
            return 0
        if A.val==B.val and self.isSameTree(A.left, B.left) and self.isSameTree(A.right, B.right):
            return 1
        else:
            return 0
        

a = Solution()
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)

out = a.isSameTree(root1, root2)
print('Is Same Tree: ', out)
