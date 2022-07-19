'''

Inorder traversal 
def inorderTraversal(self, A):
        if A is None:
            return None
        self.inorderTraversal(A.left)
        self.inorderTraversal.append(A.val)
        self.inorderTraversal(A.right)
        return self.postorderList

Created on Jul 3, 2018
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
    # @return a list of integers
    def inorderTraversal(self, A):
        stack = []
        node = A
        inOrder_list = list()
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                inOrder_list.append(node.val)
                node = node.right
        return inOrder_list


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

out = a.inorderTraversal(root)
print('In Order Traversal = ', out)


