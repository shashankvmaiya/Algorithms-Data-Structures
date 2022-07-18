'''
147. Insertion Sort List

Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.

The steps of the insertion sort algorithm:

Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs 
within the sorted list and inserts it there.
It repeats until no input elements remain.

Input: head = [4,2,1,3]
Output: [1,2,3,4]

'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def insertionSortList(self, A):
        if A.next is None:
            return A

        Ahead, Asort_prev, Asort = A, A, A.next
        while Asort:
            Atemp = Ahead
            if Atemp.val > Asort.val:
                Asort_prev.next = Asort.next
                Asort.next = Atemp
                Ahead = Asort
                Asort = Asort_prev.next
            else:
                while Atemp.next != Asort and Atemp.next.val<Asort.val:
                    Atemp = Atemp.next
                if Atemp.next == Asort:
                    Asort_prev = Asort
                    Asort = Asort.next
                else:
                    Asort_prev.next = Asort.next
                    Asort.next = Atemp.next
                    Atemp.next = Asort
                    Asort = Asort_prev.next
        return Ahead



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


input = [4, 2, 7, 8, 1, 3, 5, 6]
#input = [3, 5, 6]
input = [4, 4, 7, 1, 1, 3, 5, 6]
ll = LinkedList()
for i in input:
    ll.add_node(i)

print ("Input LL: ")
ll.list_print()

output = a.insertionSortList(ll.head)

print ("Output LL: ")
count = 0
while output != None and count < 10:
    print(output.val)
    output = output.next
    count+=1
