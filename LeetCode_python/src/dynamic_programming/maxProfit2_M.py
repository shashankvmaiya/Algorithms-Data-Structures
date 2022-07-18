'''
122. Best Time to Buy and Sell Stock II

Question: What is the max profit you can make given the price array of a stock and you can buy/sell multiple times
E.g., A = [2, 1, 10, 9, 2, 6, 5] ==> Answer = (10-1) + (6-2) = 9+6 = 15

Solution: Dynamic Programming
    - Dn = Max profit at n
    - Dn+1 = Dn + (x(n+1) - x(n)) if x(n+1) > x(n)
           = Dn else
'''

class Solution:
    def maxProfit(self, A):
        n = len(A)
        if n<2:
            return 0
        max_profit = 0
        Dn = max(max_profit, A[1]-A[0])
        D1 = Dn
        for i in range(2, n):
            Dn = D1 + (A[i] - A[i-1]) if A[i]>=A[i-1] else D1
            D1 = Dn
        return Dn

a = Solution()
inp = [2, 1, 2, 9, 2, 6, 5]
inp = [3, 4, 5]
inp = [4, 1, 4, 1, 4, 1]
inp = [5, 4, 3, 2]
inp = [5, 4]
inp = [2, 3]
str = a.maxProfit(inp)
print ('Max Profit = ', str)
