'''
Preorder Traversal
def preorderTraversal(self, A):
    if A is None:
        return None
    self.preOrderList.append(A.val)
    self.preorderTraversal(A.left)
    self.preorderTraversal(A.right)
    return self.preOrderList

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
        self.preOrderList = list()
        
    def preorderTraversal(self, A):
        if A is None:
            return None
        preOrderList = [];
        stack = [A]
        while stack:
            curr_node = stack.pop()
            preOrderList.append(curr_node.val)
            if curr_node.right:
                stack.append(curr_node.right)
            if curr_node.left:
                stack.append(curr_node.left)
        return preOrderList
    
    # Preorder traversal using recursion 
    def preorderTraversal_recursive(self, A):
        if A is None:
            return None
        self.preOrderList.append(A.val)
        self.preorderTraversal_recursive(A.left)
        self.preorderTraversal_recursive(A.right)
        return self.preOrderList
        

a = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

out = a.preorderTraversal(root)
print('Preorder Traversal: ', out)