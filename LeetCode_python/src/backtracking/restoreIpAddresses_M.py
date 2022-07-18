'''
93. Restore IP Addresses

Question: Given a string of numbers, output all the possible IP addresses. Conditions being
	IP address format: A.B.C.D (4 numbers with each number <256)
	 
Solution: 
	1. Function ip_check to check validity (A, B, C, D <255)
	2. Split the input number string into 4 using 3 for loops and appropriate checks to break 
	from the loop if there are not sufficient number in the string for the remaining numbers 
	
Backtracking Solution:
	- Add solution to the result list if there are 4 individual ips and we have covered the entire string
	- If either one of the two conditions are met and the other is not, the ip is not valid  
	- For each ip - upto 3 possible extensions with 1 number, 2 numbers and 3 numbers

'''
class Solution_backtrack:
	def restoreIpAddresses(self, s):
		result = []
		self.dfs(s, 0, 0, '', result)
		return result
	def dfs(self, string, index, ip_ctr, ip, result):
		if ip_ctr==4 and index!=len(string):
			return
		if index==len(string) and ip_ctr!=4:
			return
		if ip_ctr==4 and index==len(string):
			result.append(ip[:-1])
			return
		self.dfs(string, index+1, ip_ctr+1, ip+string[index]+'.', result)
		if int(string[index])!=0 and index<len(string)-1:
			self.dfs(string, index+2, ip_ctr+1, ip+string[index:index+2]+'.', result)
			if int(string[index:index+3])<=255 and index<len(string)-2:
				self.dfs(string, index+3, ip_ctr+1, ip+string[index:index+3]+'.', result)

class Solution:
	# @param A : string
	# @return a list of strings
	def restoreIpAddresses(self, A):
		n =len(A)
		if n<4:
			return []
		ip_addresses = list()
		num_list = [0]*4
		# Range (1, 4) because, max number = 255 which is 3 digits
		for p1 in range(1, 4):
			num_list[0] = A[:p1]
			num_digits_rem = n-p1
			if num_digits_rem<3:
				break
			for p2 in range(1, 4):
				num_list[1] = A[p1:p1+p2]
				num_digits_rem = n-p1-p2
				if num_digits_rem<2:
					break
				for p3 in range(1, 4):
					num_list[2] = A[p1+p2:p1+p2+p3]
					num_digits_rem = n-p1-p2-p3
					if num_digits_rem<1:
						break
					num_list[3] = A[p1+p2+p3:]
					curr_ip = '.'.join(num_list)
					if self.is_valid(curr_ip):
						ip_addresses.append(curr_ip)
		return ip_addresses

	def is_valid(self, ip):
		numbers = ip.split('.')
		#print(numbers)
		for i in numbers:
			if int(i)>255:
				return False
			elif len(i) != len(str(int(i))):
				return False
		return True

a = Solution_backtrack()
inp = '010010'
str = a.restoreIpAddresses(inp)
print ('IP Addresses = ', str)
