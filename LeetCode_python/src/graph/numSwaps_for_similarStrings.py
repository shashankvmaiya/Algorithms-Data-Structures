'''
Question: 
Strings A and B are K-similar (for some non-negative integer K) if we can swap the positions of two letters in A exactly 
K times so that the resulting string equals B.

Given two anagrams A and B, return the smallest K for which A and B are K-similar.
Input: A = "aabc", B = "abca"
Output: 2

Solution: 
    - Treat each string as a node
    - Breadth First search. 
    - For each node, swap the first misplaced letter with all its true position 

Created on May 12, 2019

@author: smaiya
'''


class Solution:
    def kSimilarity(self, A, B):
        
        def one_char_change(x):
            i=0 # i is the first mis-matched index
            while x[i]==B[i]:
                i+=1
            for j in range(i+1, len(B)):
                if x[j]==B[i]: # Swapping to get the correct character at the i-th position 
                    yield x[:i]+x[j]+x[i+1:j]+x[i]+x[j+1:]
            
            
        queue, visited = [(A, 0)], {A}
        while queue:
            curr, count = queue.pop(0)
            if curr==B:
                return count
            for st in one_char_change(curr):
                if st not in visited:
                    visited.add(st)
                    queue.append((st, count+1))