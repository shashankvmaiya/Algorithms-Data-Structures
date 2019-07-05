'''
Question: Find the largest value in each row of a binary tree.
Input: 

          1
         / \
        3   2
       / \   \  
      5   3   9 

Output: [1, 3, 9]

Solution: 
    - BFS and find the max value at each level


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
    def largestValues(self, root):
        if not root:
            return []
        
        queue = [root]
        max_value = []
        
        while queue:
            next_queue, curr_max = [], float('-Inf')
            
            for node in queue:
                curr_max = max(curr_max, node.val)
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            queue = next_queue
            max_value.append(curr_max)
        
        return max_value