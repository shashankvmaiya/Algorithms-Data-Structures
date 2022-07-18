'''
Question: Given a binary tree, return all root-to-leaf paths.
Note: A leaf is a node with no children.
Input:
   1
 /   \
2     3
 \
  5
Output: ["1->2->5", "1->3"]

Solution: 
    - Breadth first traversal. Keep storing the path. If leaf, then add it to result

Created on Apr 14, 2019

@author: smaiya
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root):
        if not root:
            return []
        result = []
        queue = [(root, str(root.val))]
        while queue:
            node, path = queue.pop(0)
            if node.left is None and node.right is None:
                result.append(path)
            if node.left:
                queue.append((node.left, path+'->'+str(node.left.val)))
            if node.right:
                queue.append((node.right, path+'->'+str(node.right.val)))
        return result
