'''
328. Odd Even Linked List

Q: Given a singly linked list, group all odd nodes together followed by the even nodes. 
Please note here we are talking about the node number and not the value in the nodes.
Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL

Solution: 
    1. Split into 2 linked list - one connecting even nodes, and the second connecting odd nodes
    2. Connect the even list and the odd list 
Created on Mar 19, 2019
@author: smaiya
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def oddEvenList(self, head):
        if head is None or head.next is None or head.next.next is None:
            return head
        
        # Split into 2 linked list
        odd_list, even_list, even_list_head = head, head.next, head.next
        
        while even_list.next and even_list.next.next:
            odd_list.next, even_list.next = even_list.next, even_list.next.next
            odd_list, even_list = odd_list.next, even_list.next
        if even_list.next:
            odd_list.next = even_list.next
            odd_list = odd_list.next
        
        # Connect the even and the odd list 
        odd_list.next, even_list.next = even_list_head, None
        return head
    
    
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


input = ([5, 4, 3, 2 ,1])
ll = LinkedList()
for i in input:
    ll.add_node(i)

print ("Input LL: ")
ll.list_print()


output = Solution().oddEvenList(ll.head)

print ("Output LL: ")
while output != None:
    print(output.val)
    output = output.next