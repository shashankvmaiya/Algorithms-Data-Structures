'''
Question: Check if the LInked List is a palindrome

SOlution: 
    1. Starting from the mid-point, reverse all the links, i.e., from A->B->C->D->E to A->B->C<-D<-E
    2. STart comparing values using two pointers one from the head, and the other from the tail   

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
	# @param A : head node of linked list
	# @return an integer
	def lPalin(self, A):
		A_fwd = A
		# Count number of elements in the Linked list
		count = 0
		while A_fwd != None:
			A_fwd = A_fwd.next
			count += 1
		if count == 1:
			return 1
		elif count == 2:
			if A.val == A.next.val:
				return 1
			else:
				return 0
		mid = int(count/2) + 1
		#print(count, mid)

		A_prev = A
		A_curr = A_prev.next
		A_next = A_curr.next
		count = 1
		while A_next != None:
			A_prev = A_curr
			A_curr = A_next
			A_next = A_next.next
			count += 1
			if count >= mid:
				A_curr.next = A_prev

		A_rev = A_curr
		A_fwd = A
		for i in range(mid-1):
			#print(A_rev.val, A_fwd.val)
			if A_rev.val != A_fwd.val:
				return 0
			else:
				A_rev = A_rev.next
				A_fwd = A_fwd.next
		return 1




a = Solution()
node1 = ListNode('A')
node2 = ListNode('B')
node3 = ListNode('C')
node4 = ListNode('D')
node5 = ListNode('E')
#node6 = ListNode('E')
node7 = ListNode('D')
node8 = ListNode('C')
node9 = ListNode('B')
node10 = ListNode('A')
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node7
#node6.next = node7
node7.next = node8
node8.next = node9
node9.next = node10
str = a.lPalin(node1)
print ('Is it a Palindrome = ', str)
