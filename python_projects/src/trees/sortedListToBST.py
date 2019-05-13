'''
Question: Given a singly linked list where elements are sorted in ascending order, 
convert it to a height balanced BST.

Solution:
    - Create a dummy BST via Breadth First Traversal by adding a Tree Node for every 
    node in the Linked List. This would create a balanced BST
    - THen using In order traversal, change the value of the BST with the value of linked list
    
Created on Mar 31, 2019

@author: smaiya
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST(self, head):
        if head is None:
            return None
        list_node = head
        bst_root = TreeNode(0)
        queue = [bst_root]
        list_node = list_node.next
        # Create a balanced BST of size n using breadth-first approach 
        while list_node:
            curr_node = queue.pop(0)
            curr_node.left = TreeNode(0)
            queue.append(curr_node.left)
            list_node = list_node.next
            if list_node:
                curr_node.right = TreeNode(0)
                queue.append(curr_node.right)
                list_node = list_node.next
                
        # Inorder traversal to insert elements
        stack = []
        node = bst_root
        list_node = head
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                node.val = list_node.val
                list_node = list_node.next
                node = node.right
                
        return bst_root
    
    
class LinkedList:
    def __init__(self, head=None):
        self.head = head
    def add_node(self, data):
        new_node = ListNode(data)
        new_node.next = self.head
        self.head = new_node
    def list_print(self):
        node = self.head
        while node:
            print(node.val)
            node = node.next

a = Solution()


inp = [-10,-3,0,5,9]
ll = LinkedList()
for i in inp:
    ll.add_node(i)

print ("Input LL: ")
ll.list_print()

#ll.head.next.next.next.next.next.next = ll.head
ll.head.next.next.next = ll.head
output = a.sortedListToBST(ll.head)