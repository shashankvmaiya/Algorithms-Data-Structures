'''
Remove Nth Node From End of List

Q: Given a linked list, remove the n-th node from the end of list and return its head.
Given linked list: 1->2->3->4->5, and n = 2. the linked list becomes 1->2->3->5.

Solution: 
    Maintain 2 linked list. A and A_minus_n to get the node to delete in one loop
    A_minus_n starts incrementing after n counts
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
    def removeNthFromEnd(self, A, B):
        if B<=0:
            return A
        Atemp = A
        Atemp_minus_n = A
        count = 0
        while Atemp:
            if count>B:
                Atemp_minus_n = Atemp_minus_n.next
            count+=1
            Atemp = Atemp.next
        if B>=count:
            A = A.next
        else:
            Atemp_minus_n.next = Atemp_minus_n.next.next
        return A


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

(input, n) = ([5, 4, 3, 2 ,1], 2)
(input, n) = ([5, 4, 3, 2 ,1], 0)
(input, n) = ([5, 4, 3, 2 ,1], 5)
(input, n) = ([5, 4, 3, 2 ,1], 8)
ll = LinkedList()
for i in input:
    ll.add_node(i)

print ("Input LL: ")
ll.list_print()

output = a.removeNthFromEnd(ll.head, n)

print ("Output LL: ")
while output != None:
    print(output.val)
    output = output.next
