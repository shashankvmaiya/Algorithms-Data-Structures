'''
Question: Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.

Solution: DFS approach
        - Use pre order traversal DFS (BFS can also be used)
        - If node is a leaf node, then add the string into result array   
    
Created on May 12, 2019

@author: smaiya
'''
# Definition for a  binary tree node
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root):
        result = []
        self.dfs(root, result, '')
        return sum([int(x) for x in result])
        
    def dfs(self, node, result, num_str):
        if not node:
            return
        if not node.left and not node.right:
            result.append(num_str+str(node.val))
            return
        if node.right:
            self.dfs(node.right, result, num_str+str(node.val))
        if node.left:
            self.dfs(node.left, result, num_str+str(node.val))