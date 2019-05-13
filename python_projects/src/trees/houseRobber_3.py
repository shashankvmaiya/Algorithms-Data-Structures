'''
Question: It will automatically contact the police if two directly-linked houses were broken into on the same night.
==> Thief cannot steal nodes that link each other
Determine the maximum amount of money the thief can rob tonight without alerting the police.
All values in the nodes positive. 
Input: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \ 
 1   3   1

Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.

Solution:
    - Post order traversal. Children node processed before the parent
    - Return max loot including the current node and excluding the current node
    - Result = max (including, excluding)
    - node.including = node.val + node.left.excluding + node.right.excluding
    - node.excluding = max(node.left.including, node.left.excluding) + max(right...)

Created on Apr 21, 2019

@author: smaiya
'''


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
        
class Solution:
    def rob(self, root):
        if root is None: 
            return 0
        
        loot = self.dfs(root)
        return max(loot)
    
    def dfs(self, node):
        if node is None:
            return [0, 0]
        
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        
        including = node.val+left[1]+right[1]
        excluding = max(left)+max(right)
        return [including, excluding]
    
    
    