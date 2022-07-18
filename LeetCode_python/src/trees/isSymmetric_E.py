'''
101. Symmetric Tree

Created on Jul 3, 2018
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

Solution: Use Breadth First Traversal
    - Store pairs of nodes which are mirror in the queue, i.e., (left_node, right_node)
    - So, instead of having 2^n nodes at level n, you will have 2^(n-1) tuples at level n
    - Compare the values of these tuples 
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
    def isSymmetric(self, root):
        if root is None:
            return True
        
        queue = [(root.left, root.right)]
        while queue:
            nodes = queue.pop(0)
            node_left, node_right = nodes
            if node_left is None and node_right is None:
                continue
            if node_left is None or node_right is None:
                return False
            if node_left.val == node_right.val:
                # Check for None is done while popping
                queue.append((node_left.left, node_right.right))
                queue.append((node_left.right, node_right.left))
            else:
                return False
        return True
    
    def isSymmetric2(self, A):
        if A is None or (A.left is None and A.right is None):
            return 1
        if A.left is None or A.right is None:
            return 0
        left_queue, right_queue = [A.left], [A.right]
        while left_queue:
            curr_left_node = left_queue.pop(0)
            curr_right_node = right_queue.pop(0)
            if curr_left_node.val != curr_right_node.val:
                return 0
            if curr_left_node.left and curr_right_node.right:
                left_queue.append(curr_left_node.left)
                right_queue.append(curr_right_node.right)
            elif (curr_right_node.right and curr_left_node.left is None) or (curr_left_node.left and curr_right_node.right is None):
                return 0
            
            if curr_left_node.right and curr_right_node.left:
                left_queue.append(curr_left_node.right)
                right_queue.append(curr_right_node.left)
            elif (curr_right_node.left and curr_left_node.right is None) or (curr_left_node.right and curr_right_node.left is None):
                return 0
        return 1
            



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

out = a.isSymmetric(root)
print('Is Symmetric? = ', out)
