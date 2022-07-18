'''
Quora Online Test: Given list of n individuals with certain skill level, and a target team skill sum k, 
how many different ways can you for a team of 3? The team of 3 must have a skill sum of k
 E.G. [1, 1, 1, 2, 2, 2, 3, 3, 3] & target sum = 4
 - 1+1+2 --- 3x3 = 9 ways
 - 2+2 --- 3 ways
Total of 12 ways

Solution: 
    - Create a A_unique and A_count arrays consisting of the number of unique elements in A
    - Get the number of combinations assuming all 3 have different skill level (num_i*num_j*num_k))
    - Get the number of combinations assuming 2 have same skill level and 1 is different 
    - Get the number of combinations assuming all 3 have same skill level 

Created on Apr 14, 2019

@author: smaiya
'''


class Solution:
    def num_3sum(self, A, k):
        A.sort()
        A_count = {}
        for k in A:
            A_count[k] = A_count.get(k, 0)+1
            
        return 0 
        
        
        
        
        
        
        
inp = [1, 1, 1, 2, 2, 2, 3, 3, 3], k = 4

out = Solution().num_3sum(inp, k)
print('Number of teams = ', out)
