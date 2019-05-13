class Solution:
	# @param A : list of integers
	# @return a list of integers
	def lszero2(self, A):
		n = len(A)
		sum_count_list = [dict() for x in range(2)]
		sum_count_list[0][A[0]] = 1
		(max_length, max_end_idx) = (1, 0) if A[0] == 0 else (-1, -1)
		for i in range(1, n):
			num = A[i]
			for sum in sum_count_list[(i-1)%2]:
				sum_count_list[i%2][sum+num] = sum_count_list[(i-1)%2][sum] + 1
			if 0 not in sum_count_list[(i-1)%2]:
				sum_count_list[i%2][num] = 1
			if 0 in sum_count_list[i%2] and sum_count_list[i%2][0] > max_length:
				max_length = sum_count_list[i%2][0]
				max_end_idx = i
			sum_count_list[(i-1)%2].clear()
			#print (sum_count_list)
		#print (max_length, max_end_idx)
		if max_end_idx == -1:
			return []
		else:
			return A[max_end_idx-max_length+1:max_end_idx+1]

	def lszero(self, A):
		n = len(A)
		sum_1toi = [A[0]]
		for i in range(1, n):
			sum_1toi.append(sum_1toi[i-1]+A[i])
		sum_check = dict()
		(max_length, max_start_idx, max_end_idx) = (0, -1, -1)
		#print(sum_1toi)
		for i in range(n):
			sum = sum_1toi[i]
			if sum in sum_check or sum == 0:
				idx = 0 if sum==0 else sum_check[sum]
				(max_length, max_start_idx, max_end_idx) = (i-idx+1, idx, i) if (i-idx+1) > max_length else (max_length, max_start_idx, max_end_idx)
			else:
				sum_check[sum] = i+1
		#print(sum_check)
		#print (max_start_idx, max_end_idx, max_length)
		if max_length == 0:
			return []
		else:
			return A[max_end_idx-max_length+1:max_end_idx+1]


a = Solution()
inp = [0, -10 ]
inp = [1, 2, -2, 4, -4]
str = a.lszero(inp)
print ('Largest Continuous Sequence = ', str)
