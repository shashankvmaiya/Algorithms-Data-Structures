'''
Created on Jul 3, 2018
Given a binary tree, invert the binary tree and return it. 

Input
     0
    / \
   2   4

Output:
     0
    / \
   4   2
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
    # @return the root node in the tree
    def invertTree(self, A):
        # Breadth-first traversal. Swap left and right nodes
        if A is None or (A.left is None and A.right is None):
            return A
        queue = [A]
        while queue:
            curr_node = queue.pop(0)
            curr_node.left, curr_node.right = curr_node.right, curr_node.left
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right) 
        return A


a = Solution()
node1, node2, node3, node4, node5 = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5)
node6, node7, node8, node9 = TreeNode(6), TreeNode(7), TreeNode(8), TreeNode(9)

#root = TreeNode(1)
#root.left = TreeNode(2)
#root.right = TreeNode(3)

root = node7
node7.left = node2
node2.left = node1
node2.right = node4
node4.left = node3
node4.right = node5
node5.right = node6


out = a.invertTree(root)
print('Inverted Tree = ', out.val, out.right.val)
