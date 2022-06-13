'''
You are given a tree (i.e. a connected, undirected graph that has no cycles) rooted 
at node 0 consisting of n nodes numbered from 0 to n - 1. The tree is represented 
by a 0-indexed array parent of size n, where parent[i] is the parent of node i. Since 
node 0 is the root, parent[0] == -1.

You are also given a string s of length n, where s[i] is the character assigned to node i.

Return the length of the longest path in the tree such that no pair of adjacent nodes 
on the path have the same character assigned to them.

Input: parent = [-1,0,0,1,1,2], s = "abacbe"
     0a
    / \
  2a   1b
  / \   \ 
 5e  3c  4b

Output: 3
Explanation: The longest path where each two adjacent nodes have different characters in 
the tree is the path: 0 -> 1 -> 3. The length of this path is 3, so 3 is returned.
It can be proven that there is no longer path that satisfies the conditions. 

Created on June 11, 2022
@author: smaiya
'''
import heapq
class Solution:
    def longestPath(self, parent, s):
        self.max_length = 0
        self.children = {}
        self.s = {}
        for i, p in enumerate(parent):
            if i>=0:
                if p in self.children:
                    self.children[p].append(i)
                else:
                    self.children[p] = [i]
            self.s[i] = s[i]
        self.dfs(0)
        return self.max_length

    def dfs(self, node):
        children = self.children[node] if node in self.children else []
        min_heap = []
        for c in children:
            n = self.dfs(c)
            if self.s[c] != self.s[node]:
                if len(min_heap)<2:
                    heapq.heappush(min_heap, n)
                else:
                    heapq.heappushpop(min_heap, n)
        
        max_len_node = max(min_heap)+1 if min_heap else 1
        max_len_subtree = min_heap[0] + min_heap[1] + 1 if len(min_heap)==2 else 0
        self.max_length = max(self.max_length, max_len_node, max_len_subtree)

        return max_len_node

parent = [-1,0,0,1,1,2]
s = "abacbe"
ans = Solution().longestPath(parent, s)
print('Longest Path = ', ans)