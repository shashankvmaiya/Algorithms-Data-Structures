'''
Question: Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Solution: Dynamic Programming. O(n^2)
	- Maintain an array P[i, j] = True if Si to Sj is a palindrome, else False
	- Populate P[i, j] array starting from length 1 palindrome length to max length n. 
	- Keep checking and updating max_length and the associated palindrome
	Method to get P[i, j]: 
		P[i, i] = True (Length 1 Palindrome)
		P[i, i+1] = (Si == Si+1) (Length 2 Palindrome)
		P[i, j] = P[i+1, j-1] && (Si == Sj)
'''

class Solution:
	# @param A : string
	# @return a strings
	def longestPalindrome(self, A):
		n = len(A)
		palindrome_array = [[False]*n for i in range (n)]
		palindrome = A[0]
		max_length = 1
		# Palindromes of length 1
		for i in range(n):
			palindrome_array[i][i] = True
		# Palindromes of length 2
		for i in range(n-1):
			if A[i]==A[i+1]:
				palindrome_array[i][i+1] = True
				if max_length == 1:
					palindrome = A[i:i+2]
					max_length = 2
		
		# Checking for palindromes of length 3 onwards
		for length in range(3, n+1):
			for i in range(0, n-length+1):
				if palindrome_array[i+1][i+length-2] and A[i]==A[i+length-1]:
					palindrome_array[i][i+length-1] = True
					if max_length < length:
						max_length = length
						palindrome = A[i:i+length]
				#print(length, i, palindrome)
		return palindrome


a = Solution()
inp = 'caba'
str = a.longestPalindrome(inp)
print ('Longest Palindrome = ', str)
