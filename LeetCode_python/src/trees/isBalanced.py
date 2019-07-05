'''
Created on Jul 3, 2018
Given a binary tree, determine if it is height-balanced.
Height-balanced binary tree : is defined as a binary tree in which the depth of the two subtrees 
of every node never differ by more than 1
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
    def isBalanced(self, A):
        if A is None or (A.left is None and A.right is None):
            return 1
        queue = [A]
        while queue:
            curr_node = queue.pop(0)
            if curr_node.left != None:
                queue.append(curr_node.left)
            elif curr_node.right != None:
                if curr_node.right.left !=None or curr_node.right.right !=None:
                    return 0
                    
            if curr_node.right != None:
                queue.append(curr_node.right)
            elif curr_node.left != None:
                if curr_node.left.left !=None or curr_node.left.right !=None:
                    return 0
                
        return 1



a = Solution()
node1, node2, node3, node4, node5 = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5)
node6, node7, node8, node9 = TreeNode(6), TreeNode(7), TreeNode(8), TreeNode(9)

node1A, node2A, node3A, node4A, node5A = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5)
node6A, node7A, node8A, node9A = TreeNode(6), TreeNode(7), TreeNode(8), TreeNode(9)

root = node4
node4.left = node2
node4.right = node6
node2.left = node1
node2.right = node3
node6.right = node7
node3.right = node9

out = a.isBalanced(root)
print('Is Balanced? = ', out)

