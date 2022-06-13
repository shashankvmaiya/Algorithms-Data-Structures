'''
You are given the root of a binary tree with n nodes. Each node is uniquely assigned a 
value from 1 to n. You are also given an integer startValue representing the value of 
the start node s, and a different integer destValue representing the value of the 
destination node t.

Find the shortest path starting from node s and ending at node t. Generate step-by-step 
directions of such path as a string consisting of only the uppercase letters 'L', 'R', 
and 'U'. Each letter indicates a specific direction:

'L' means to go from a node to its left child node.
'R' means to go from a node to its right child node.
'U' means to go from a node to its parent node.
Return the step-by-step directions of the shortest path from node s to node t.

Created on June 11, 2022
@author: smaiya
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class TreeConstruct:
    def get_tree(self, nodes):
        if not nodes:
            return None
        
        root = TreeNode(nodes[0])
        queue = [root]
        idx = 1
        while queue:
            n = queue.pop(0)
            if idx<len(nodes) and nodes[idx]:
                n.left = TreeNode(nodes[idx])
                queue.append(n.left)
            idx+=1

            if idx<len(nodes) and nodes[idx]:
                n.right = TreeNode(nodes[idx])
                queue.append(n.right)
            idx+=1
        
        return root




class Solution:
    def getDirections(self, root, startValue, destValue):
        queue = [(root, [(root, 'X')])]
        start_ancestors, dest_ancestors = None, None
        while queue:
            node, ancestors = queue.pop(0)
            
            if node.val == startValue:
                start_ancestors = ancestors
            if node.val == destValue:
                dest_ancestors = ancestors
                
            if start_ancestors and dest_ancestors:
                return self.find_path(start_ancestors, dest_ancestors)
            
            if node.left:
                queue.append((node.left, ancestors + [(node.left, 'L')]))
            if node.right:
                queue.append((node.right, ancestors + [(node.right, 'R')]))
    
    def find_path(self, s, d):
        for i in range(min(len(s), len(d))):
            if s[i][0].val == d[i][0].val:
                lca, level = s[i][0].val, i
            else:
                break
        
        up_path = 'U'*(len(s)-level-1)
        down_path = ''.join([d[i][1] for i in range(level+1, len(d))])
        path = up_path + down_path
        return path


a = Solution()
nodes = [5,1,2,3,None,6,4]
root = TreeConstruct().get_tree(nodes)
out = a.getDirections(root, 3, 6)

print('Direction = ', out)
