'''
 Sadhana Amazon Assessment: 6/1/2018
 Question: find the most frequented word excluding words from 'ignore_list' 
'''
import re
class Solution:
	# @param A : integer
	# @return an integer
	def mostFrequentWord(self, A, B):
		exclude_map = dict()
		for words in B:
			exclude_map[words.lower()] = 1

		literature_map = dict()
		inp_word_list = re.split('[^a-zA-Z]+', A)
		max_count = 0
		for words in inp_word_list:
			words = words.lower()
			if words not in exclude_map:
				literature_map[words] = literature_map.get(words, 0)+1
				max_count = max(max_count, literature_map[words])

		most_frequent_word_list = list()
		for words in literature_map:
			if literature_map[words] == max_count:
				most_frequent_word_list.append(words)
		return most_frequent_word_list

a = Solution()
inp1 = 'Jack and jill went to the market to get some cheese. Jack\'s and Jill\'s cheese is tasty'
inp2 = ['is', 'a', 'are', 'to']
str = a.mostFrequentWord(inp1, inp2)
print ('Most Frequent Word = ', str)
