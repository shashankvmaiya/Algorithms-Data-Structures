'''
Created on Jul 7, 2018
Lowest common ancestor : the lowest common ancestor (LCA) of two nodes v and w in a tree or directed acyclic graph (DAG) is the lowest 
(i.e. deepest) node that has both v and w as descendants. 
@author: smaiya
'''


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def find_lca(self, a, b):
        n = min(len(a), len(b))
        output=a[0]
        for i in range(n):
            if a[i].val==b[i].val:
                output=a[i]
            else:
                break
        return output
    
    def lowestCommonAncestor(self, root, p, q):
        queue = [(root, [root])]
        p_found, q_found = False, False
        while queue:
            node, ancestors = queue.pop(0)
            
            if node.val==p.val:
                p_found=True
                p_ancestors = ancestors
            if node.val==q.val:
                q_found=True
                q_ancestors = ancestors
            if p_found and q_found:
                return self.find_lca(p_ancestors, q_ancestors)
            
            if node.left:
                queue.append((node.left, ancestors+[node.left]))
            if node.right:
                queue.append((node.right, ancestors+[node.right]))


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
out = a.lowestCommonAncestor(root, node9, node8)
print('Lowest Common Ancestor = ', out.val)

