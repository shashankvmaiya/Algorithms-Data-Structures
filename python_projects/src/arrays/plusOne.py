class Solution:
	# @param A : list of integers
	# @return a list of integers
	def plusOne(self, A):
		if A == [0]:
			return [1]
		A_plus_one = []
		flag = False
		for digit in A:
			if digit != 0 or flag:
				flag = True
				A_plus_one.append(digit)
		n = len(A_plus_one)
		A_plus_one[n-1] = (A_plus_one[n-1] + 1)%10
		all_zero_flag = True
		carry_flag = True if A_plus_one[n-1] == 0 else False
		for idx in range(n-2, -1, -1):
			if A_plus_one[idx+1] == 0 and carry_flag:
				A_plus_one[idx] = (A_plus_one[idx] + 1)%10
			else:
				all_zero_flag = False
				carry_flag = False
				break

		if all_zero_flag and A_plus_one[0] == 0:
			A_plus_one.insert(0, 1)

		return A_plus_one


a = Solution()
inp = [0, 0, 0, 0, 0, 9, 9, 9, 9, 9]
inp = [0]
inp = [3, 0, 6, 4, 0]
inp = [1, 9, 9, 9, 9, 9]
str = a.plusOne(inp)
print ('Plus One = ', str)
