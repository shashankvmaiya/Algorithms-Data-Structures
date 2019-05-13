class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return a list of integers
	def twoSum(self, A, B):
		n = len(A)
		remainder = dict()
		for i in range(n):
			num = A[i]
			if num in remainder:
				index2 = i+1
				index1 = remainder[num]
				return [index1, index2]
			else:
				remainder[B-num] = remainder.get(B-num, i+1)
		return []

a = Solution()
inp = [2, 3, 11, 15, 3]
inp2 = 6
str = a.twoSum(inp, inp2)
print ('Two Sum = ', str)
