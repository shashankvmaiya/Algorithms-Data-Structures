'''
Created on Jul 8, 2018
Populate each next pointer to point to its next right node. If there is no next right node, 
the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Solution: Breadth first traversal. Connect the nodes of the same level starting from left
@author: smaiya
'''

# Definition for a  binary tree node
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        # Breadth first traversal
        if not root:
            return None
        queue =[root]
        while queue:
            prev_node = None
            for i in range(len(queue)):
                curr_node = queue.pop(0)
                if prev_node:
                    prev_node.next = curr_node
                prev_node = curr_node
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
            curr_node.next = None
        return root

a = Solution()
node1, node2, node3, node4, node5 = TreeLinkNode(1), TreeLinkNode(2), TreeLinkNode(3), TreeLinkNode(4), TreeLinkNode(5)
node6, node7, node8, node9 = TreeLinkNode(6), TreeLinkNode(7), TreeLinkNode(8), TreeLinkNode(9)

node1A, node2A, node3A, node4A, node5A = TreeLinkNode(1), TreeLinkNode(2), TreeLinkNode(3), TreeLinkNode(4), TreeLinkNode(5)
node6A, node7A, node8A, node9A = TreeLinkNode(6), TreeLinkNode(7), TreeLinkNode(8), TreeLinkNode(9)

root = node4
node4.left = node2
node4.right = node6
node2.left = node1
node2.right = node3
node6.right = node7
node3.right = node9

out = a.connect(root)
print(' Tree with Right node connected', out.val, out.left.val, out.left.next.val, out.right.val)

