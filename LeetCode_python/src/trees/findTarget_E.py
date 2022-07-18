'''
Question: Given a binary search tree T, where each node contains a positive integer, and an integer K, 
you have to find whether or not there exist two different nodes A and B such that A.value + B.value = K
Your solution should run in linear time and not take memory more than O(height of T)

Solution: Use two traversals - 1. fwd in order (which will give values in increasing order) and 
2. rev in order traversal (giving values in decreasing order). 
If the sum of the two values < target, increment the fwd traversal, else decrement the rev traversal. 
Memory = 2*O(height of T) used to store the nodes in the 2 stacks

Created on Apr 5, 2019

@author: smaiya
'''

# Definition for a  binary tree node
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findTarget(self, root, k):
        if not root: 
            return False
        if root.left is None and root.right is None:
            return False
        stack_fwd, stack_rev = [], []
        node_fwd, node_rev = root, root
        
        while node_fwd:
            stack_fwd.append(node_fwd)
            node_fwd = node_fwd.left
        while node_rev:
            stack_rev.append(node_rev)
            node_rev = node_rev.right
        
        curr_fwd = stack_fwd.pop()
        curr_rev = stack_rev.pop()
        node_fwd = curr_fwd.right
        node_rev = curr_rev.left
        while (curr_fwd is not curr_rev) and (stack_fwd or node_fwd) and (stack_rev or node_rev):
            if (curr_fwd.val+curr_rev.val==k):
                return True
            if (curr_fwd.val+curr_rev.val<k):
                if node_fwd:
                    stack_fwd.append(node_fwd)
                    node_fwd = node_fwd.left
                else:
                    curr_fwd = stack_fwd.pop()
                    node_fwd = curr_fwd.right
            else:
                if node_rev:
                    stack_rev.append(node_rev)
                    node_rev = node_rev.right
                else:
                    curr_rev = stack_rev.pop()
                    node_rev = curr_rev.left
        
        return False