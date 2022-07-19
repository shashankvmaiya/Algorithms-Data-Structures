'''
103. Binary Tree Zigzag Level Order Traversal

Given a binary tree, return the zigzag level order traversal of its nodes values.
(ie, from left to right, then right to left for the next level and alternate between).

Solution: Breadth First Traversal.
    - Process all nodes in the same level
    - Store them in a list
    - Reverse them or not depending on a flag and append them to the final zig_zag_list

Created on Jul 7, 2018
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
    # @return a list of list of integers
    
    def zigzagLevelOrder(self, root):
        if root is None:
            return []
        queue = [root]
        flag = 1
        curr_list, zig_zag_list = [], []
        while queue:
            for i in range(len(queue)): # Processes all the nodes of the same level
                node = queue.pop(0)
                curr_list.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            zig_zag_list.append(curr_list[::flag])
            curr_list=[]
            flag*=-1
        return zig_zag_list
    
    
    def zigzagLevelOrder2(self, A):
        curr_list, zig_zag_list = [], []
        stack, stack_next = [A], []
        l_first = True
        while stack:
            curr_node = stack.pop()
            curr_list.append(curr_node.val)
            if l_first:
                if curr_node.left:
                    stack_next.append(curr_node.left)
                if curr_node.right:
                    stack_next.append(curr_node.right)
            else:
                if curr_node.right:
                    stack_next.append(curr_node.right)
                if curr_node.left:
                    stack_next.append(curr_node.left)
            if stack == []:
                zig_zag_list.append(curr_list)
                curr_list = []
                stack = stack_next
                stack_next = []
                l_first = not l_first
        return zig_zag_list
                    
        



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
node1.right = node8

#out = a.flatten(root)
out = a.zigzagLevelOrder(root)
print('Zig Zag Level Order = ', out)
