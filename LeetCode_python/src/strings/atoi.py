import re
class Solution:
	# @param A : string
	# @return an integer
	def atoi(self, A):
		A.lstrip()
		A.rstrip()
		first_word = A.split()
		nums = re.findall('^([-+]*[0-9]+)\s*', first_word[0])
		int_value = 0
		try:
			int_value = int(nums[0])
			if int_value>=2**31:
				int_value = 2**31-1
			elif int_value<=-2**31-1:
				int_value = -(2**31)
		except:
			return 0
		return int_value


a = Solution()
inp = '+7'
str = a.atoi(inp)
print ('String to Int = ', str)
