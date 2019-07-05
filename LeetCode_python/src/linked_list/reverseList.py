'''
Question: Given a singly linked list and an integer K, reverses the nodes of the
list K at a time and returns modified linked list.
Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 and K=2
Output: 2 -> 1 -> 4 -> 3 -> 6 -> 5

Solution: 
    - Reverse all links except from Ki+1
    - Link from (Ki+1).next = K(i+1)
    - Return the head of the Kth link
    E.g., Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> NULL and K=3
    Output = (to 6)<- 1 <- 2 <- 3  (to 9)<- 4 <- 5 <- 6  (to NULL)<- 7 <- 8 <- 9
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
    def reverseList(self, A, B):
        if B == 1:
            return A
        prev, node = None, A
        result = None
        count = 0
        k_end, k_end_prev = None, None
        while node:
            count+=1
            #print(count, node.val)
            if count==B:
                result = node # Return the Bth node
            if count%B==1:  # If Bi+1 -st node
                k_end, k_end_prev = node, k_end
                node.next, prev, node = None, node, node.next
            elif count%B==0 and count>B: # Starting from 2B-th node, start connecting it to the Bi+1 st node
                node.next, k_end_prev.next, prev, node = prev, node, node, node.next
            else: # Just reverse the links
                node.next, prev, node = prev, node, node.next
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

(input, n) = ([6, 5, 4, 3, 2 ,1], 2)
(input, n) = ([6, 5, 4, 3, 2 ,1], 3)
(input, n) = (range(25, 0, -1), 5)
#(input, n) = ([6, 5, 4, 3, 2, 1], 1)
ll = LinkedList()
for i in input:
    ll.add_node(i)

print ("Input LL: ")
ll.list_print()

output = a.reverseList(ll.head, n)

print ("Output LL: ")
while output != None:
    print(output.val)
    output = output.next
