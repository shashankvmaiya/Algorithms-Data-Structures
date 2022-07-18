'''
86. Partition List

Question: Given a linked list and a value x, partition it such that all nodes less than x 
come before nodes greater than or equal to x.
E.g., Input: 1->4->3->2->5->2 and x = 3,
Output: 1->2->2->4->3->5

Solution: 
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def partition(self, A, B):
        lesser, greater, node = None, None, A
        
        while node:
            if node.val>=B:
                if greater:
                    greater.next = node
                    greater = greater.next
                else:
                    greater, greater_head = node, node
                greater.next, node = None, node.next
                
            else:
                if lesser:
                    lesser.next = node
                    lesser = lesser.next
                else:
                    lesser, lesser_head = node, node
                lesser.next, node = None, node.next
        if lesser is None or greater is None:
            return A
        lesser.next = greater_head
        return lesser_head





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

(input, n) = ([2, 5, 2, 3, 4, 1], 3)
#(input, n) = ([2, 5, 2, 3, 4, 1], 6)
#(input, n) = ([2, 5, 2, 3, 4, 1], 1)

ll = LinkedList()
for i in input:
    ll.add_node(i)

print ("Input LL: ")
ll.list_print()

output = a.partition(ll.head, n)

print ("Output LL: ")
while output != None:
    print(output.val)
    output = output.next
