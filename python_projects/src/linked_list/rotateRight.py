# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def rotateRight(self, A, B):
        n = 0
        Atemp = A
        while Atemp:
            n+=1
            Atail = Atemp
            Atemp = Atemp.next
        rotate = B%n
        if rotate ==0:
            return A
        Atemp = A
        count = 1
        while count<n-rotate:
            Atemp = Atemp.next
            count+=1
        A_right_shift = Atemp.next
        Atemp.next = None
        Atail.next = A
        return A_right_shift


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

output = a.rotateRight(ll.head, n)

print ("Output LL: ")
while output != None:
    print(output.val)
    output = output.next
