'''
21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the 
nodes of the first two lists.

Return the head of the merged linked list.
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A, B):

        if A is None:
            return B
        if B is None:
            return A
        if A.val <= B.val:
            result = ListNode(A.val)
            A = A.next
        else:
            result = ListNode(B.val)
            B = B.next
        result_temp = result

        while A != None or B != None:
            if A is None:
                new_node = ListNode(B.val)
                B = B.next
            elif B is None:
                new_node = ListNode(A.val)
                A = A.next
            elif A.val <= B.val:
                new_node = ListNode(A.val)
                A = A.next
            elif B.val < A.val:
                new_node = ListNode(B.val)
                B = B.next
            result_temp.next = new_node
            result_temp = result_temp.next
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


(input1, input2) = ([23, 22, 20, 8, 5], [15, 11, 8, 4])
#(input1, input2) = ([1], [1])

ll1 = LinkedList()
for i in input1:
    ll1.add_node(i)
ll2 = LinkedList()
for i in input2:
    ll2.add_node(i)

print ("Input LL1: ")
ll1.list_print()

print ("Input LL2: ")
ll2.list_print()

output = a.mergeTwoLists(ll1.head, ll2.head)

print ("Output LL: ")
while output != None:
    print(output.val)
    output = output.next
