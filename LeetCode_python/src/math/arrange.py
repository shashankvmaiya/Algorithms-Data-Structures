'''
Created on Jul 19, 2018
Rearrange a given array so that Arr[i] becomes Arr[Arr[i]] with O(1) extra space.
@author: smaiya
'''

class Solution:
    # @param A : list of integers
    # Modify the array A which is passed by reference. 
    # You do not need to return anything in this case. 
    def arrange(self, A):
        n = len(A)
        # Encoding two numbers (A[i] as LSB and A[A[i]] as MSB) at A[i]
        for i in range(n):
            A[i] = A[i] + (A[A[i]]%n)*n
        for i in range(n):
            A[i] = int(A[i]/n)

inp = [5, 2, 1, 1, 4, 1, 7, 2, 8, 0]
Solution().arrange(inp)
print('Rearranged A = ', inp)
