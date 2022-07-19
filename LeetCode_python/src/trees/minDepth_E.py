'''
111. Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from 
the root node down to the nearest leaf node.

BFS. Keep updating the min_depth as we go one level lower. 
Terminate and return the moment a node doesnt have a leaf 

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
    # @return an integer
    def minDepth(self, root):
        if root is None:
            return 0
        min_depth = 1
        queue = [root]
        while queue:
            next_queue = []
            for node in queue:
                if not node.left and not node.right:
                    return min_depth
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            queue = next_queue
            min_depth+=1
        return min_depth


a = Solution()
node1, node2, node3, node4, node5 = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5)
node6, node7, node8, node9 = TreeNode(6), TreeNode(7), TreeNode(8), TreeNode(9)

#root = node7
#node7.left = node2
#node2.left = node1
#node2.right = node4
#node4.left = node3
#node4.right = node5
#node5.right = node6

root = node1
node1.left = node2
node2.right = node3

out = a.minDepth(root)
print('Minimum Depth = ', out)
