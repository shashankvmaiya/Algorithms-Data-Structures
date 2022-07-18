'''
Question: Design a data structure that supports the following two operations:
void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. 
A . means it can represent any one letter.
addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true

Solution: 
    - Use a Trie
    - Search using a dfs approach

Created on Jun 1, 2019

@author: smaiya
'''

class TrieNode:
    def __init__(self):
        self.end_of_word = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        """
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c]=TrieNode()
            node=node.children[c]
        node.end_of_word=True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.dfs(self.root, word, 0)
    
    def dfs(self, node, word, idx):
        if idx == len(word):
            return node.end_of_word
        if word[idx] in node.children:
            return self.dfs(node.children[word[idx]], word, idx+1)
        if word[idx]=='.':
            for c in node.children:
                if self.dfs(node.children[c], word, idx+1):
                    return True
        return False
            
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
