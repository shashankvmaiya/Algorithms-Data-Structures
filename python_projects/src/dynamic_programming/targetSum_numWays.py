'''
Question: You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. 
Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.
Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.

Solution: DFS or Dynamic Programming
    - DFS- keep calling the function with updated target and quit after covering the entire array
    - DP
        - Store a matrix dp[i][j] which denotes the number of ways to arrive at number j at time step i
        - Range of i = 0 to len(nums)
        - Range of j = -sum(nums) to sum(nums)
        - dp[i+1][j+nums[i]] += dp[i][j]
        - dp[i+1][j-nums[i]] += dp[i][j]
Created on May 12, 2019

@author: smaiya
'''
class Solution:
    def findTargetSumWays_dfs(self, nums, S):
        self.count = 0
        self.dfs(nums, S, 0)
        return self.count
    def dfs(self, vector, target, idx):
        if idx==len(vector):
            if target==0:
                self.count+=1
            return
        
        self.dfs(vector, target-vector[idx], idx+1)
        self.dfs(vector, target+vector[idx], idx+1)
        
    def findTargetSumWays_dp(self, nums, S):
        max_sum = sum(nums)
        if max_sum < S or -max_sum>S: # nums contain only positive numbers
            return 0
        n = len(nums)
        m = 2*max_sum+1 # Range of sum = -max_sum to max_sum including 0
        dp = [[0]*m for _ in range(n+1)]
        
        dp[0][max_sum] = 1 # max_sum corresponds to sum=0 index
        
        for i in range(n):
            for j in range(nums[i], m-nums[i]):
                dp[i+1][j+nums[i]] += dp[i][j]
                dp[i+1][j-nums[i]] += dp[i][j]
                
        return dp[-1][max_sum+S] # index max_sum corresponds to sum = 0 ==> sum = S will be at max_sum+S
    
    