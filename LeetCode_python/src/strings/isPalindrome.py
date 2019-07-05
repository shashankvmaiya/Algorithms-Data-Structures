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
