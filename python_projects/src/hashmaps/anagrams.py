'''
Q: Given an array of strings, group anagrams together.
Solution: Store sorted words as hashmap keys and the index of the output anagram_list as values 
'''

class Solution:
	# @param A : tuple of strings
	# @return a list of list of integers
	def anagrams(self, A):
		sorted_word_list = dict()
		anagram_list = list()
		counter = 0
		for i, word in enumerate(A):
			letter_list = sorted(list(word))
			sorted_word = ''.join([x for x in letter_list])
			if sorted_word in sorted_word_list:
				anagram_list[sorted_word_list[sorted_word]].append(word)
			else:
				sorted_word_list[sorted_word] = counter
				anagram_list.append([word])
				counter += 1
		return anagram_list


a = Solution()
inp = ['cat', 'dog', 'god', 'tca', 'blah']
str = a.anagrams(inp)
print ('Anagrams = ', str)
