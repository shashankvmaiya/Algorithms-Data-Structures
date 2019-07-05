'''
Question: Reverse a linked list from position m to n. 
E.g., Given 1->2->3->4->5->NULL, m = 2 and n = 4, return 1->4->3->2->5->NULL

Solution:
    - Advance till m-th node and start swapping all links between mth and nth node
    - Once you reach the n-th node, do the remaining plumb work.
        - (m-1) -> n and m -> (n+1)
    - Only corner case is when m=1. Then, there is no (m-1) node. The starting node or the 
    node to return would be the n-th node
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @param C : integer
    # @return the head node in the linked list
    def reverseBetween(self, A, B, C):
        if B>=C:
            return A
        count = 0
        prev, node, Ahead = None, A, A
        while node:
            count+=1
            if count == B:
                start_prev = prev
                start_node = node
            if B<count<=C: # Reverse all links between B and C
                node.next, node, prev = prev, node.next, node
            else:
                prev, node = node, node.next
            if count == C: 
                if start_prev is None: # If B=1, then the head would be the C-th index of the linked list 
                    start_node.next = node
                    Ahead = prev
                else:
                    start_prev.next, start_node.next = prev, node
                break
        return Ahead


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

(input, m, n) = ([5, 4, 3, 2 ,1], 2, 4)
(input, m, n) = ([5, 4, 3, 2 ,1], 2, 2)
(input, m, n) = ([5, 4, 3, 2 ,1], 2, 5)
#(input, m, n) = ([5, 4, 3, 2 ,1], 1, 5)
#(input, m, n) = ([5, 4, 3, 2 ,1], 1, 3)
ll = LinkedList()
for i in input:
    ll.add_node(i)

print ("Input LL: ")
ll.list_print()

output = a.reverseBetween(ll.head, m, n)

print ("Output LL: ")
while output != None:
    print(output.val)
    output = output.next
