'''
Question: Given a singly linked list, modify the value of first half nodes such that :
1st node’s new value = the last node’s value - first node’s current value
2nd node’s new value = the second last node’s value - 2nd node’s current value,
If the length L of linked list is odd, then the first half implies at first floor(L/2) nodes. 
So, if L = 5, the first half refers to first 2 nodes.

Solution: 
    - Locate the mid point of the linked list
    - Reverse the second half of the list
    - First pointer from the start and second pointer from end, modify the first half value 
    till they reach the mid point
    - Reverse back the second half of the list
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def subtract(self, A):
        if A==None or A.next ==None:
            return A

        # Locating the mid node
        mid, fast = A, A
        while(fast.next and fast.next.next):
            mid = mid.next
            fast = fast.next.next

        # Reversing the second half of the list
        prev, node = None, mid # slow = Mid node
        while node:
            node.next, node, prev = prev, node.next, node
        end = prev

        # Subtract operation. fwd half val = fwd half val - rev half val
        fwd, rev = A, end # starting and ending nodes
        while rev != mid:
            fwd.val = rev.val - fwd.val
            fwd, rev = fwd.next, rev.next

        # Reversing back the second half link
        prev, node = None, end # prev stores the ending node link
        while node!=None:
            node.next, node, prev = prev, node.next, node
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


input = [5, 4, 3, 2, 1]
#input = [6, 5, 4, 3, 2, 1]
ll = LinkedList()
for i in input:
    ll.add_node(i)

print ("Input LL: ")
ll.list_print()

output = a.subtract(ll.head)

print ("Output LL: ")
while output != None:
    print(output.val)
    output = output.next
