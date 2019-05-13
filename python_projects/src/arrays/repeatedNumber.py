class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        flag = dict()
        for num in A:
            if num in flag:
                return num
            else:
                flag[num] = 1

a = Solution()
inp = [3, 4, 1, 4, 1]
str = a.repeatedNumber(inp)
print ('Repeated Number = ', str)
