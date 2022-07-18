'''
49. Group Anagrams

Q: Given an array of strings, group anagrams together.

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Solution: Store sorted words as hashmap keys and the index of the output anagram_list as values 
'''

class Solution:
    # @param A : tuple of strings
    # # @return a list of list of integers
    def anagrams(self, A):
        anagram_list = dict()
        for i, word in enumerate(A):
            letter_list = sorted(list(word))
            sorted_word = ''.join([x for x in letter_list])
            if sorted_word in anagram_list:
                anagram_list[sorted_word].append(word)
            else:
                anagram_list[sorted_word] = [word]
        return list(anagram_list.values())


a = Solution()
inp = ['cat', 'dog', 'god', 'tca', 'blah']
str = a.anagrams(inp)
print ('Anagrams = ', str)
