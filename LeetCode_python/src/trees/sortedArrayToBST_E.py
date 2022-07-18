'''
Created on Jul 3, 2018
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
@author: smaiya
'''

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : tuple of integers
    # @return the root node in the tree
    def sortedArrayToBST(self, A):
        n = len(A)
        
        # Create a balanced BST of size n using breadth-first approach 
        bst_root = TreeNode(0)
        queue = [bst_root]
        num_nodes = 1
        while num_nodes < n:
            curr_node = queue.pop(0)
            curr_node.left = TreeNode(0)
            num_nodes+=1
            queue.append(curr_node.left)
            if num_nodes < n:
                curr_node.right = TreeNode(0)
                num_nodes+=1
                queue.append(curr_node.right)
                
        # In order Traversal to insert the elements from the sorted array 
        stack = []
        node = bst_root
        counter = 0
        while (stack or node):
            if (node):
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                node.val = A[counter]
                counter+=1
                node = node.right
            
        return bst_root
      
      
a = Solution()
inp = [1, 2, 3]  
inp = [1]
out = a.sortedArrayToBST(inp)
#print('Ordered BST = ', out.val, out.left.val, out.right.val)
print('Ordered BST = ', out.val)


