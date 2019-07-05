'''
Question: Find the max(j-i) such that A[i] <= A[j]
Eg. A = [3, 5, 4, 2], then A[j=2] = 4, A[i=0] = 3 ==> Output =2 

Solution: 
	1. Get LMin[n] where ith element consists of min (1 to i)
	2. Get RMax[n] where ith element consists of max (j to n)
	3. For each min element LMin i, find the max j in RMax. Max of j-i is the answer

'''

class Solution:
	# @param A : tuple of integers
	# @return an integer
	def maximumGap(self, A):
		n = len(A)
		LMin = [0]*n
		LMin[0] = A[0]
		for i in range(1, n):
			LMin[i] = min(LMin[i-1], A[i])
		RMax = [0]*n
		RMax[-1] = A[-1]
		for j in range(n-2,-1,-1):
			RMax[j] = max(RMax[j+1], A[j])

		(i, j) = (0, 0)
		max_distance = 0
		while i<n and j < n:
			#print(i, j, max_distance)
			if RMax[j] >= LMin[i]:
				max_distance = max(j-i, max_distance)
				j=j+1
			else:
				i=i+1
		return max_distance

a = Solution()
inp = [100, 100, 100, 100, 100]
str = a.maximumGap(inp)
print ('Max Gap = ', str)
