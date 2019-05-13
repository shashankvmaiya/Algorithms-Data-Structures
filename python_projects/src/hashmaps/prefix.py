'''
Created on Jul 7, 2018
shortest unique prefix to represent each word in the list.
Input: [zebra, dog, duck, dove]
Output: {z, dog, du, dov}
This is a tree question. Can be solved using Trie. 
@author: smaiya
'''


class Solution:
    # @param A : list of strings
    # @return a list of strings
    def prefix(self, A):
        prefix_dict = dict()
        for word in A:
            n = len(word)
            for i in range(n):
                prefix_dict[word[:i+1]] = prefix_dict.get(word[:i+1], 0)+1
        
        shortest_prefix = [];
        for word in A:
            n = len(word)
            for i in range(n):
                if prefix_dict[word[:i+1]] == 1:
                    shortest_prefix.append(word[:i+1])
                    break
        return shortest_prefix


a = Solution()
inp = ['zebra', 'dog', 'duck', 'dove']
str = a.prefix(inp)
print ('Shortest Unique Prefix = ', str)

