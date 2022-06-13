'''
Given the root of a binary tree, return the number of nodes where the value of the node 
is equal to the average of the values in its subtree.

Note:
The average of n elements is the sum of the n elements divided by n and 
rounded down to the nearest integer.

Input: root = [4,8,5,0,1,null,6]
     4
    / \
   8   5
  / \   \ 
 0   1   6
Output: 5
Explanation: 
For the node with value 4: The average of its subtree is (4 + 8 + 5 + 0 + 1 + 6) / 6 = 24 / 6 = 4.
For the node with value 5: The average of its subtree is (5 + 6) / 2 = 11 / 2 = 5.
For the node with value 0: The average of its subtree is 0 / 1 = 0.
For the node with value 1: The average of its subtree is 1 / 1 = 1.
For the node with value 6: The average of its subtree is 6 / 1 = 6.

Created on June 11, 2022
@author: smaiya
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def averageOfSubtree(self, root):
        if root is None:
            return 0
        self.result = 0
        self.dfs(root)
        return self.result
        
    def dfs(self, node):
        if node is None:
            return 0, 0
        
        left_total, left_n = self.dfs(node.left)
        right_total, right_n = self.dfs(node.right)
        
        total = left_total + right_total + node.val
        n = left_n + right_n + 1
        avg = total // n
        if avg == node.val:
            self.result+=1
        return total, n

