'''
212. Word Search II

Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are 
horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Input: board = 
[["o","a","a","n"],
["e","t","a","e"],
["i","h","k","r"],
["i","f","l","v"]], 
words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]


Input: board = 
[["a","b"],
["c","d"]], 
words = ["abcb"]
Output: []

Solution:


Created on July 20, 2022
@author: smaiya
'''
from typing import Dict, Any, List
from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.end_of_word = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c]=TrieNode()
            node = node.children[c]
        node.end_of_word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        words_trie = Trie()
        self.result = set()
        self.m, self.n = len(board), len(board[0])
        self.num_words = len(words)
        for w in words:
            words_trie.insert(w)
        
        node = words_trie.root
        for row in range(self.m):
            for col in range(self.n):
                self.extend_if_possible(board, row, col, node, '')

        return list(self.result)

    def dfs(self, board, row, col, node, word):
        if self.num_words==0: # If there are no more words to search, exit early
            return
        if node.end_of_word:
            self.result.add(word)
            self.num_words-=1
            node.end_of_word = False # do not search for the same word again
        
        self.extend_if_possible(board, row-1, col, node, word)
        self.extend_if_possible(board, row+1, col, node, word)
        self.extend_if_possible(board, row, col-1, node, word)
        self.extend_if_possible(board, row, col+1, node, word)

    def extend_if_possible(self, board, row, col, node, word):
        if row < 0 or row >= self.m or col < 0 or col >= self.n:
            return 
        c = board[row][col]
        if c in node.children:
            board[row][col] = '#' # Marking the position as visited using a special character
            self.dfs(board, row, col, node.children[c], word+c)
            board[row][col] = c



board = [["a","b","e"],["b","c","d"]]
words = ["abcdeb"]

ans = Solution().findWords(board, words)
