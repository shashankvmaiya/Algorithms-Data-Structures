'''
8. String to Integer (atoi)

Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer 
(similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

- Read in and ignore any leading whitespace.
- Check if the next character (if not already at the end of the string) is '-' or '+'. 
Read this character in if it is either. This determines if the final result is negative or 
positive respectively. Assume the result is positive if neither is present.

- Read in next the characters until the next non-digit character or the end of the input is reached.
The rest of the string is ignored.

- Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). 
If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).

- If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the 
integer so that it remains in the range. Specifically, integers less than -231 should be 
clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.

- Return the integer as the final result.

Input: s = "   -42"
Output: -42
Explanation:
Step 1: "   -42" (leading whitespace is read and ignored)
            ^
Step 2: "   -42" ('-' is read, so the result should be negative)
             ^
Step 3: "   -42" ("42" is read in)
               ^
The parsed integer is -42.
Since -42 is in the range [-231, 231 - 1], the final result is -42.

'''

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
