'''
200. Number of Islands

Question: Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is
formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
Input:
11000
11000
00100
00011

Output: 3

Solution: Use Union Find Algorigthm
    - Union Find to store disjoint sets
    - Initialize by storing all lands as an islan
    - Union any adjacent land (1)
    - Number of islands = Number of subsets

Created on May 12, 2019

@author: smaiya
'''

class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
        uf = UnionFind(grid)
        rows, cols = len(grid), len(grid[0])
        
        for i in range(rows):
            for j in range(cols): # Merging all adjacent land
                if i>0 and grid[i][j] == '1' and grid[i-1][j]=='1':
                    uf.union(i*cols+j, (i-1)*cols+j)
                if i<rows-1 and grid[i][j] == '1' and grid[i+1][j]=='1':
                    uf.union(i*cols+j, (i+1)*cols+j)
                if j>0 and grid[i][j] == '1' and grid[i][j-1]=='1':
                    uf.union(i*cols+j, i*cols+(j-1))
                if j<cols-1 and grid[i][j] == '1' and grid[i][j+1]=='1':
                    uf.union(i*cols+j, i*cols+(j+1))
        return uf.subsets
        
class UnionFind:
    def __init__(self, grid):
        rows, cols = len(grid), len(grid[0])
        self.parent = {} # Would inidcate the island index
        self.subsets = 0 # Number of islands
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=='1': # Every land, is initialized to an island
                    self.subsets += 1
                    self.parent[i*cols+j] = i*cols+j
    def union(self, x, y):
        s = self.find(x)
        t = self.find(y)
        if s!=t:
            self.subsets-=1 # If we are merging two different islands, then reduce by 1
            self.parent[s] = t
        
    def find(self, x):
        while x != self.parent[x]:
            x = self.parent[x]
        return x

