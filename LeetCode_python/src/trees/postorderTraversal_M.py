'''
Postorder traversal
def postorderTraversal(self, A):
        if A is None:
            return None
        self.postorderTraversal(A.left)
        self.postorderTraversal(A.right)
        self.postorderList.append(A.val)
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
    def __init__(self):
        self.postorderList = list()
    
    def postorderTraversal(self, A):
        if A is None:
            return None
        postOrderList = [];
        stack, last_node_visited, node = [], None, A
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                peek_node = stack[-1]
                if peek_node.right and last_node_visited != peek_node.right:
                    node = peek_node.right
                else:
                    postOrderList.append(peek_node.val)
                    last_node_visited = stack.pop()
        return postOrderList
    
    def postorderTraversal_recursive(self, A):
        if A is None:
            return None
        self.postorderTraversal_recursive(A.left)
        self.postorderTraversal_recursive(A.right)
        self.postorderList.append(A.val)
        return self.postorderList
        


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

out = a.postorderTraversal(root)
print('Post Order Traversal = ', out)

