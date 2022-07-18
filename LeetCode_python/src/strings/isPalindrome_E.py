'''
125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase 
letters and removing all non-alphanumeric characters, it reads the same forward and 
backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

'''

import re
class Solution:
	# @param A : string
	# @return an integer
	def isPalindrome(self, A):
		try:
			#A_alnum_only = re.sub('[^a-zA-z0-9]+', '', A)
			A_alnum_only = ''.join(e.lower() for e in A if e.isalnum())
			A_alnum_only_rev = A_alnum_only[::-1]
			if A_alnum_only_rev == A_alnum_only:
				return 1
			else:
				return 0
		except:
			return 0

a = Solution()
inp = 'A man, a plan, a canal: Panama'
inp = ''
str = a.isPalindrome(inp)
print ('Is it a Palindrome = ', str)
