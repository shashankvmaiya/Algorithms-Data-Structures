'''
2. Add Two Numbers

Q: You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Solution: Ensure that carry is taken care of till the very end.
E.g., 999 + 1 = 1000
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
    def addTwoNumbers(self, A, B):
        if A is None:
            return B
        if B is None:
            return A

        (carry, remainder) = divmod(A.val+B.val, 10)
        result = ListNode(remainder)
        result_temp = result
        A, B = A.next, B.next
        while A or B:
            if A is None:
                (carry, remainder) = divmod(B.val+carry, 10)
                B = B.next
            elif B is None:
                (carry, remainder) = divmod(A.val+carry, 10)
                A = A.next
            else:
                (carry, remainder) = divmod(A.val+B.val+carry, 10)
                A = A.next
                B = B.next
            new_node = ListNode(remainder)
            result_temp.next = new_node
            result_temp = result_temp.next
        if carry:
            new_node = ListNode(carry)
            result_temp.next = new_node
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

(input1, input2) = ([3, 4, 2], [4, 6, 5])
(input1, input2) = ([3, 4, 2], [8, 6, 5])
(input1, input2) = ([1, 5, 4], [])
(input1, input2) = ([], [1, 5, 4])
(input1, input2) = ([2, 3], [5, 1, 5, 4])

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

output = a.addTwoNumbers(ll1.head, ll2.head)

print ("Output LL: ")
while output != None:
    print(output.val)
    output = output.next
