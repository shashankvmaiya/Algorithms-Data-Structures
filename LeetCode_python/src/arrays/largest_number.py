'''
Q: Largest number that can be formed by concatenating the individual numbers in the list
Eg. [3, 30, 34, 5, 9] --> 9534330

Solution: Sort the numbers based on 'key' function. Concatenate the sorted list
The function to be sorted: repeat the numbers x times so that we can compare the numbers with identical length
E.g. 12 vs. 121. 
key_function(12) -->121212
key_function(121)-->121121 
'''


class Solution:
	# @param A : tuple of integers
	# @return a strings
	def largestNumber(self, A):
		max_num = max(A)
		max_num_digits = 2*len(str(max_num))
		inp = dict()
		key_step = float(1.0/(len(A)+1))
		for num in A:
			num_digits = len(str(num))
			num_str = str(num)
			key_str = num_str + num_str*(max_num_digits-num_digits)
			key = int(key_str[:max_num_digits])
			while key in inp:
				key = key + key_step
			inp[key] = num

		largest_number = ''
		for k, v in sorted(inp.items(), reverse=True):
			#print (k, v)
			largest_number = largest_number+str(v)
		return str(int(largest_number))



a = Solution()
inp = [ 782, 240, 409, 678, 940, 502, 113, 686, 6, 825, 366, 686, 877, 357, 261, 772, 798, 29, 337, 646, 868, 974, 675, 271, 791, 124, 363, 298, 470, 991, 709, 533, 872, 780, 735, 19, 930, 895, 799, 395, 905 ]
str = a.largestNumber(inp)
print ('Largest Number = ', str)
