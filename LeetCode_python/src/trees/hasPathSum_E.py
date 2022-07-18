'''
112. Path Sum

Created on Jul 3, 2018
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values 
along the path equals the given sum.
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
    # @param B : integer
    # @return an integer
    def hasPathSum(self, A, B):
        # Do a pre-order traversal to visit each node (Breadth-first traversal can be done too using queues)
        # Check the sum at the node if it is a leaf
        if A is None:
            return 0
        stack = [A]
        sum_stack = [A.val]
        while stack:
            curr_node = stack.pop()
            curr_sum = sum_stack.pop()
            if curr_node.left is None and curr_node.right is None:
                if curr_sum == B:
                    return 1
            if curr_node.right != None:
                stack.append(curr_node.right)
                sum_stack.append(curr_node.right.val+curr_sum)
            if curr_node.left != None:
                stack.append(curr_node.left)
                sum_stack.append(curr_node.left.val+curr_sum)
        return 0


a = Solution()
node1, node2, node3, node4, node5 = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5)
node6, node7, node8, node9 = TreeNode(6), TreeNode(7), TreeNode(8), TreeNode(9)

node1A, node2A, node3A, node4A, node5A = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5)
node6A, node7A, node8A, node9A = TreeNode(6), TreeNode(7), TreeNode(8), TreeNode(9)

root = node1
node1.left = node2
node1.right = node2A
node2.left = node3
node2.right = node4
node2A.left = node4A
node2A.right = node3A

out = a.hasPathSum(root, 10)
print('Has Path Sum? = ', out)

