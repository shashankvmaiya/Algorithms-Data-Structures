'''
Question: You are given coins of different denominations and a total amount of money amount. 
Write a function to compute the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1
Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1

Solution: Dynamic Programming
    - D(n) = min(D(n-c0), D(n-c1), ... D(n-ck))+1 where ck are the coin denominations

Created on Apr 5, 2019

@author: smaiya
'''

class Solution:
    def coinChange(self, coins, amount):
        if amount ==0:
            return 0
        
        coins.sort()
        # If the lowest denomination > target amount, then return -1
        if coins[0]>amount:
            return -1
        Dn = [-1 for i in range(amount+1)]
        
        # If the coin denomination exists, then minimum number of coins = 1 
        for coin in coins:
            if coin<=amount:
                Dn[coin] = 1
        
        # Start from minimum denomination+1, find Dn for every n
        n=coins[0]+1
        while n <= amount:
            for coin in coins:
                if coin<=n and Dn[n-coin] != -1:
                    Dn[n] = (Dn[n-coin]+1) if Dn[n]==-1 else  min(Dn[n], Dn[n-coin]+1)
            n+=1
        return Dn[amount]

inp = [1, 2, 5]
op = Solution().coinChange(inp, 11)
print ('Minimum number of coins = ', op)