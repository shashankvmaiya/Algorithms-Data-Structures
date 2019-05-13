class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        words = A.split()
        if words == []:
            return 0
        return len(words[-1])

a = Solution()
inp = '  '
str = a.lengthOfLastWord(inp)
print ('Length of Last Word = ', str)
