'''
151. Reverse Words in a String

Question: Given an input string, reverse the string word by word.
Input: "the sky is blue"
Output: "blue is sky the"
Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

Solution: String operations - 1. split()  2. [::-1], 3. ' '.join()
'''
class Solution:
    # @param A : string
    # @return string
    def reverseWords(self, s):
        if not s:
            return ''
        rev_words = ' '.join(s.split()[::-1])
        return rev_words

a = Solution()
inp = 'ankrqzzcel dyaiug y rkicv t'
str = a.reverseWords(inp)
print ('Reversed Words = ', str)
