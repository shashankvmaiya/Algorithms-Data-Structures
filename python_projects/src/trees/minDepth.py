'''
Created on Jul 3, 2018
Given a binary tree, find its minimum depth.
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
    def minDepth(self, A):
        if A is None:
            return 0
        elif A.left is None and A.right is None:
            return 1
        
        # Depth first traversal. Keep updating the min_depth as we go one level lower. 
        #Terminate and return the moment a node doesnt have a leaf 
        min_depth = list()
        queue = list()
        if A.left != None:
            queue.append(A.left)
            min_depth.append(2)
        if A.right !=None:
            queue.append(A.right)
            min_depth.append(2)
            
        while queue:
            curr_node = queue.pop(0)
            curr_min_depth = min_depth.pop(0)
            if curr_node.left is None and curr_node.right is None:
                return curr_min_depth
            if curr_node.left != None:
                queue.append(curr_node.left)
                min_depth.append(curr_min_depth+1)
            if curr_node.right != None:
                queue.append(curr_node.right)
                min_depth.append(curr_min_depth+1)


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
