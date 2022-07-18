'''
Linked List Cycle II

Question: Given a linked list, return the node where the cycle begins. If there is no cycle, return null

Solution: 
    - First detect the cycle and find the cycle length
        - Cycle can be detected using 2 pointers, one incremented at normal speed and the other at double the speed
        - The first time they meet, we can conclude that there is a cycle
        - Once cycle is detected, continue till they again meet to obtain the cycle length
    - Finding head of the cycle 
        - Use again 2 pointers; one at head, and the other at head + cycle_length
        - Keep advancing them till they meet at the head of the cycle 
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def detectCycle(self, A):
        if A is None or A.next == None:
            return None
        A_slow = A
        A_fast = A
        cycle_length = 0
        flag = False
        # Obtaining the cycle length
        while A_slow and A_fast and A_fast.next:
            A_slow = A_slow.next
            A_fast = A_fast.next.next
            if flag:
                # Count the cycle length
                cycle_length+=1
                if A_slow==A_fast:
                    break
            # Cycle detected: Set flag to True the first time they meet 
            if A_slow == A_fast:
                flag = True

        if not flag:
            return None

        A_back = A
        A_front = A
        # Finding the head of the cycle using 2 pointers
        for i in range(0, cycle_length):
            A_front = A_front.next

        while A_front != A_back:
            A_back = A_back.next
            A_front = A_front.next
        return A_front



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


inp = [6, 5, 4, 3, 2, 1]
inp = [4, 3, 2, 1]
ll = LinkedList()
for i in inp:
    ll.add_node(i)

print ("Input LL: ")
ll.list_print()

#ll.head.next.next.next.next.next.next = ll.head
ll.head.next.next.next = ll.head
output = a.detectCycle(ll.head)

print ("Output LL: ")
count = 0
while output != None and count < 10:
    print(output.val)
    output = output.next
    count+=1
