'''
96. Unique Binary Search Trees

Question: https://leetcode.com/problems/unique-binary-search-trees/
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?
Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
   
Solution: Dynamic Programming
    - DP[i] = Number of structures using i nodes
    - Given a root node, all values < root goes to the left half and all values > root goes to the right half
    - Hence for example #nodes = 4, #nodes for left subtree and right subtree can be (0, 3), (1, 2), (2, 1) and (3, 0) 
        - here 0 corresponds to empty tree
    - Hence dp[4] = dp[3]*dp[0]+dp[2]*dp[1]+dp[1]*dp[2]+dp[0]*dp[3]

Created on Jun 1, 2019

@author: smaiya
'''

class Solution:
    def numTrees(self, n):
        dp = [0 for i in range(n+1)]
        dp[0]=dp[1]=1
        for i in range(2, n+1):
            for j in range(i):
                dp[i] += dp[j]*dp[i-1-j]
        return dp[n]
        
        