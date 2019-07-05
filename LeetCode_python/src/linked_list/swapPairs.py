'''
Question: Given a linked list, swap every two adjacent nodes and return its head.
E.g., Input: 1->2->3->4, Output: 2->1->4->3.

Solution: 
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def swapPairs(self, head):
        if not head:
            return head
        if not head.next:
            return head
        
        result = head.next
        Aprev, A = None, head
        while A and A.next:
            Anext = A.next
            if Aprev:
                Aprev.next, Aprev, A.next, A, Anext.next  = Anext, A, Anext.next, Anext.next, A
            else:
                Aprev, A.next, A, Anext.next = A, Anext.next, Anext.next, A
        return result


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


input = [5, 4, 3, 2, 1]
#input = [6, 5, 4, 3, 2, 1]
#input = [2,1]
ll = LinkedList()
for i in input:
    ll.add_node(i)

print ("Input LL: ")
ll.list_print()

output = a.swapPairs(ll.head)

print ("Output LL: ")
while output != None:
    print(output.val)
    output = output.next
