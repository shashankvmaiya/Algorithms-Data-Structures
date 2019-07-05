'''
Question: Given a sorted linked list, delete all nodes that have duplicate numbers, 
leaving only distinct numbers from the original list
E.g.: Input: 1->2->3->3->4->4->5, Output: 1->2->5

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
    def deleteDuplicates(self, A):
        prev, node = None, A
        duplicate_flag = False
        while node.next:
            # Deleting the >=2nd repeated elements
            if node.val == node.next.val:
                duplicate_flag = True
                node.next = node.next.next
                if node.next is None: # Reached the end of the linked list
                    if prev is None: # If linked list with single repeating values
                        return None
                    else: # Deleting the first element as well, if we reached the end of the linked list
                        prev.next = None
            else:
                # Deleting the first element if it was a duplicate
                if duplicate_flag:
                    if prev is None: # Staring elements are repeated
                        A, node = A.next, node.next
                    else:
                        prev.next, node = node.next, node.next
                    duplicate_flag = False
                else:
                    prev, node = node, node.next
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

input = [4, 4, 2, 2, 2, 1, 1, 1, 1, 1, 1, 0]
input = [4, 4, 2, 2, 2, 1, 0, 0]
#input = [4, 4, 2, 2, 2, 1, 1, 1, 1, 1, 1, 0, 0]
#input = [6, 5, 4, 4, 2, 2, 2, 1, 1, 1, 1, 1, 1, 0, 0]
#input = [5, 4, 4, 3, 3, 2, 1]
#input = [3, 2, 1, 1, 1]
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
