'''
Question: For a given array A, check if there exists i, j such that A[i]-A[j] = k for i not equal to j
A = [1, 5, 3], k = 2, i, j = 1, 2

Solution: Use hashmap
	- For each element in A[j], store the value = A[j] + k 
	- Go over all the remainders and check if any of them is present in the main array
'''

class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return an integer
	def diffPossible(self, A, B):
		remainder = dict()
		for i in A:
			if i in remainder and B==0:
				return 1
			else:
				remainder[i] = i+B

		for k in remainder:
			if remainder[k] in A and B!=0:
				return 1
		return 0

a = Solution()
inp, inp2 = [1, 5, 3, 4, 9], 2
inp, inp2 = [1, 3, 4, 4, 5], 0
inp, inp2 = [1, 3, 4, 6, 5], 0
inp, inp2 = [1, 3, 5, 7, 5], 1
str = a.diffPossible(inp, inp2)
print ('Diff Possible = ', str)
