'''
Created on Jul 31, 2018

@author: smaiya
'''
class Solution:
    # @param A : list of integers
    # @return an integer
    def maxcoin(self, A):
        n = len(A)
        if n==1:
            return A[0]
        elif n==2:
            return max(A)
        elif n==3:
            return max(A[0], A[2]) + min(A)
        
        Atemp = A
        coins_total = [0, 0]
        player_idx = 0
        for i in range(n):
            if len(Atemp) == 3:
                if Atemp[-1] > Atemp[0]:
                    selected_coin = Atemp.pop()
                else:
                    selected_coin = Atemp.pop(0)
                coins_total[player_idx] += selected_coin
                coins_total[player_idx] += min(Atemp)
                coins_total[(player_idx+1)%2] += max(Atemp)
                return coins_total[0]
            if Atemp[-1]-max(Atemp[0], Atemp[-2]) > Atemp[0]-max(Atemp[-1], Atemp[1]):
                selected_coin = Atemp.pop()
            else:
                selected_coin = Atemp.pop(0)
            coins_total[player_idx] += selected_coin
            player_idx = (player_idx+1)%2
                 


inp = [1, 4, 5, 3, 10]
out = Solution().maxcoin(inp)
print('Max Coin = ', out)

