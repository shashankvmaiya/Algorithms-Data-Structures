'''
Flatten Binary Tree to Linked List

Created on Jul 3, 2018
Given a binary tree, flatten it to a linked list in-place.
Each nodes right child points to the next node in its preorder traversal tree

Solution: 
    - Do a pre-order traversal
    - For each element, move the current right tree to the right most leaf node of the left subtree and 
    move that left subtree to the right. This shift will still preserve the preorder traversal order     
     
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
    def flatten(self, A):
        Atemp = A
        if not A:
            return
        if A.left:
            temp, A.right, A.left = A.right, A.left, None
            self.flatten(A.right)
            while A.right:
                A = A.right
            A.right = temp
            self.flatten(A.right)
            
        else:
            self.flatten(A.right)
        return Atemp
    
    def flatten_nonrecursive(self, A):
        if not A:
            return
        stack = [A]
        while stack:
            curr_node = stack.pop()
            # First insert elements in the stack to determine to order of traversal
            if curr_node.right:
                stack.append(curr_node.right)
            if curr_node.left:
                stack.append(curr_node.left)
                
            # Left subtree moved to right. Right subtree temporarily saved in temp
            temp, curr_node.right, curr_node.left = curr_node.right, curr_node.left, None
            # Go to the end of the left subtree (which has been now moved to right)
            while curr_node.right:
                curr_node = curr_node.right
            # Assign the right subtree (which has been saved in temp) to the end of this node
            curr_node.right = temp
        return A



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

#out = a.flatten(root)
out = a.flatten(root)
print('Flattened Linked List = ', out.val, out.right.val, out.right.right.val)

