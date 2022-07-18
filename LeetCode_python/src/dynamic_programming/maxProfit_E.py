'''
121. Best Time to Buy and Sell Stock

Question: What is the max profit you can make  given the price array of a stock
E.g., A = [2, 1, 10, 9, 2, 6, 5] ==> Answer = 10-1 = 9

Solution: Dynamic Programming
    Dn = max profit at time n
    Dn+1 = max(Dn, x(n+1) - curr_min) 
'''

class Solution:
    def maxProfit(self, A):
        n = len(A)
        if n<2:
            return 0
        max_profit = 0
        Dn = max(max_profit, A[1]-A[0])
        D1 = Dn
        min_price = min(A[1], A[0])
        for i in range(2, n):
            Dn = max(D1, A[i]-min_price)
            D1 = Dn
            min_price = min(min_price, A[i])
        return Dn

a = Solution()
inp = [2, 1, 2, 9, 2, 6, 5]
inp = [5, 3, 2, 1]
inp = [5, 4, 1, 2, 2, 5]
inp = [5, 4]
inp = [4, 5]
inp = [5, 4, 6]
str = a.maxProfit(inp)
print ('Max Profit = ', str)
