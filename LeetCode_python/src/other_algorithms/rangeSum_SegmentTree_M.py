'''
307. Range Sum Query - Mutable

Question: Given an integer array nums, find the sum of the elements between indices i and j (i <= j), inclusive.
The update(i, val) function modifies nums by updating the element at index i to val.
Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8

Solution: Use Segment Tree
    - Building the Tree = O(N)
        - Built via post order traversal
        - Leaf Node = single element, Root node = all the elements and remaining internal nodes = partial intervals 
        - Note that if not a leaf node, then it will always have >2 elements ==> will have left and right child
    - Update Function = O(log N)
        - Post order traversal
        - Traverse along the path till you reach the leaf node corresponding to the element
        - First, update the leaf node sum
        - Update all the parent sum
    - SumRange Function = O(log N)
        - Hybrid pre-order traversal
        

Created on May 31, 2019

@author: smaiya
'''


class SegmentTree:
    def __init__(self, start, end, sum=0, left=None, right=None):
        self.start = start
        self.end = end
        self.sum = sum
        self.left = left
        self.right = right


class NumArray:
    def __init__(self, nums):
        if nums:
            self.root = self.build(0, len(nums)-1, nums)
    def build(self, start, end, nums):
        if start==end: # Leaf Nodes with single elements
            return SegmentTree(start, end, nums[start])
        # Note that if not a leaf node, then it will always have >2 elements ==> will have left and right child
        mid = (start+end)//2
        # Post order traversal - process the child nodes first
        left = self.build(start, mid, nums) # Left child
        right = self.build(mid+1, end, nums) # Right child
        return SegmentTree(start, end, left.sum+right.sum, left, right) # Parent node 

    
    def update(self, i, val):
        self.update_tree(self.root, i, val)
    def update_tree(self, node, index, val):
        if node.start==node.end==index: # Leaf node sum updated
            node.sum=val
            return
        mid = (node.start+node.end)//2
        if index<=mid:
            self.update_tree(node.left, index, val)
        else:
            self.update_tree(node.right, index, val)
        node.sum = node.left.sum+node.right.sum # Updating the parent sum after updating the child node sum
        

    def sumRange(self, i, j):
        return self.query_tree(self.root, i, j)
    def query_tree(self, node, start, end):
        if node.start==start and node.end==end: # If query interval == node interval
            return node.sum
        
        mid = (node.start+node.end)//2
        if start>mid: # If query range completely in the right interval
            return self.query_tree(node.right, start, end)
        elif end<=mid: # If query range completely in the left interval
            return self.query_tree(node.left, start, end)
        else:
            return self.query_tree(node.left, start, mid)+self.query_tree(node.right, mid+1, end)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)