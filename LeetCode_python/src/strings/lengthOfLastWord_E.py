'''
58. Length of Last Word
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

'''
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
