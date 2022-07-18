'''
119. Pascal's Triangle II

Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Input: rowIndex = 3
Output: [1,3,3,1]

'''


class Solution:
	# @param A : integer
	# @return a list of list of integers
	def generate(self, A):
		if A<=0:
			return []
		elif A==1:
			return [[1]]
		elif A==2:
			return [[1], [1,1]]
		pascal_triangle = list()
		pascal_triangle.append([1])
		pascal_triangle.append([1, 1])
		prev_ith_row = [1,1]
		curr_ith_row = list()
		for i in range(2, A):
			curr_ith_row.append(1)
			for j in range(1, i):
				value = prev_ith_row[j]+prev_ith_row[j-1]
				curr_ith_row.append(value)
			curr_ith_row.append(1)
			pascal_triangle.append(curr_ith_row)
			prev_ith_row = curr_ith_row
			curr_ith_row=[]
		return pascal_triangle

a = Solution()
pascal_triangle = a.generate(1)
print(pascal_triangle)
