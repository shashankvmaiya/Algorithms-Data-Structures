'''
990. Satisfiability of Equality Equations

Question: Given an array equations of strings that represent relationships between variables, each string equations[i] 
has length 4 and takes one of two different forms: "a==b" or "a!=b".  Here, a and b are lowercase letters (not necessarily different) 
that represent one-letter variable names.

Return true if and only if it is possible to assign integers to variable names so as to satisfy all the given equations.
Input: ["a==b","b!=c","c==a"]
Output: false

Input: ["c==c","b==d","x!=z"]
Output: true

Solution: 
    - Use Union-Find
    - First store all the equalities in disjoint sets
    - THen check inequalities. If the two elements are part of the same set, then return False

Created on May 11, 2019

@author: smaiya
'''


class Solution:
    def equationsPossible(self, equations):
        uf = UnionFind()
        for e in equations:
            if e[1]=='=':
                uf.union(e[0], e[3])
                
        for e in equations:
            if e[1]!='=':
                if uf.find(e[0])==uf.find(e[3]):
                    return False
        return True
        
        
        
class UnionFind:
    def __init__(self):
        self.parent = {}
    def union(self, x, y):
        s = self.find(x)
        t = self.find(y)
        self.parent[t] = s  # Sets the parent of the second node to the parent of the first node
    
    # find function returns the parent of the node
    def find(self, x):
        if x in self.parent:
            while x!=self.parent[x]:
                x=self.parent[x]
        else:   # If the node is not present in the set, then initializes the parent to itself
            self.parent[x] = x
        return x

