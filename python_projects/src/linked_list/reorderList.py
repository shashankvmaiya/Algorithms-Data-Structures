'''
Question: Given L: L0 -> L1-> ... -> Ln-1 -> Ln,
reorder it to  L0 ->Ln -> L1 -> Ln-1 -> L2-> Ln-2 -> ...
E.g., Input: 1->2->3->4->5 Output: 1->5->2->4->3

Solution: 
    - Get the mid point
    - Reverse the links of the second half of the linked list 1->2->3<-4<-5
    - One link starting from head and the other starting from tail, stitch the two lists till the meet at the mid point
'''



# Definition for singly-linked list.
import math
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reorderList(self, A):
        n = 0
        node = A
        # Getting the size of list
        while node:
            n+=1
            node=node.next
        mid_point = math.ceil(n/2)
        node = A
        count = 0

        # Getting the pointer to the middle node
        while count<mid_point:
            count+=1
            if count == mid_point:
                node.next, node = None, node.next
            else:
                node=node.next

        # Reversing the second half of the list
        prev = None
        while node:
            node.next, prev, node = prev, node, node.next

        # Stitching the first half of the list with the reversed second half
        list1, list2 = A, prev
        while list1:
            if list2:
                list1.next, list2.next, list1, list2 = list2, list1.next, list1.next, list2.next
            else:
                list1.next, list1 = list2, list1.next
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

input = [8, 7, 6, 5, 4, 3, 2, 1]
input = [9, 8, 7, 6, 5, 4, 3, 2, 1]
#input = [1]
ll = LinkedList()
for i in input:
    ll.add_node(i)

print ("Input LL: ")
ll.list_print()

output = a.reorderList(ll.head)

print ("Output LL: ")
while output != None:
    print(output.val)
    output = output.next
