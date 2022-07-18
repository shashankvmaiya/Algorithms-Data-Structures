'''
Remove Duplicates from Sorted List
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. 
Return the linked list sorted as well.

'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        A_temp = A
        while A_temp.next != None:
            if A_temp.val == A_temp.next.val:
                A_temp.next = A_temp.next.next
            else:
                A_temp = A_temp.next
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

input = 'ABCDEE'
input = [5, 5, 5, 4, 4, 2, 2, 2, 1, 1, 1, 1, 1, 1, 0]
ll = LinkedList()
for i in input:
    ll.add_node(i)

print ("Input LL: ")
ll.list_print()

output = a.deleteDuplicates(ll.head)

print ("Output LL: ")
while output != None:
    print(output.val)
    output = output.next
