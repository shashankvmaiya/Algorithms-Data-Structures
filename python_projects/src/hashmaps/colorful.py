class Solution:
	# @param A : integer
	# @return an integer
	def colorful(self, A):
		A_str = str(A)
		n = len(A_str)
		if n>10:
			return 0

		prod_list = dict()
		for length in range(1, n+1):
			for idx in range(n-length+1):
				num_list = [int(i) for i in list(A_str[idx:idx+length])]
				num_prod = self.prod(num_list)
				if num_prod in prod_list:
					return 0
				else:
					prod_list[num_prod] = 1
		return 1

	def prod(self, A):
		product = 1
		for i in A:
			product *= i
		return product


a = Solution()
inp = 23
str = a.colorful(inp)
print ('Colorful = ', str)
