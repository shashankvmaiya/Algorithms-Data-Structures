'''
Question: You are given coins of different denominations and a total amount of money. 
Write a function to compute the number of combinations that make up that amount. 
You may assume that you have infinite number of each kind of coin.
Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

Solution: Dynamic Programming 
    - D(n) = D(n-c0) +  D(n-c1) + D(n-ck)) where ck are the coin denominations
    - First loop over the coin denominations to ensure we do not land up with repetitions 
    which are coin permutation of each other 
Created on Apr 5, 2019

@author: smaiya
'''


class Solution:
    def change(self, amount, coins):
        if amount==0:
            return 1
        if coins == []:
            return 0
        coins.sort()
        if coins[0]>amount:
            return 0
        
        Dn = [0 for i in range(amount+1)]
        Dn[0] = 1
        for coin in coins:
            for i in range(coin, amount+1):
                Dn[i] += Dn[i-coin]
        return Dn[amount]
    

inp = [1, 2, 5]
op = Solution().coinChange(inp, 11)
print ('Number of ways to get change= ', op)