'''
Created on Jun 30, 2018
You are given an array of N integers, A1, A2 ,..., AN. Return maximum value of f(i, j) for all 1 <= i, j <= N.
f(i, j) is defined as |A[i] - A[j]| + |i - j|, where |x| denotes absolute value of x.

Solution: 
    - |A[i] - A[j]| + |i - j| = max (X1, X2, X3, X4), where
        - X1 = A(i) + i - (A(j) + j)
        - X2 = A(i) - i - (A(j) - j)
        - X3 = A(j) + j - (A(i) + i)
        - X4 = A(j) - j - (A(i) - i)
        Out of X1, X2, X3 and X4 - only one combination would have both |A[i] - A[j]| and |i - j| positive
    - Hence store SUM = A(i)+i and DIFF = A(i)-i for all values of i 
    - Result = max(max(SUM) - min(SUM), max(DIFF)-min(DIFF))
@author: smaiya
'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        n = len(A)
        A1, A2 = list(), list()
        max1, max2, min1, min2 = None, None, None, None
        # A1 and A2 stores A(i)+i and A(i)-i respectively
        # max1/min1 = max(A1) and min(A1)
        # Max Abs Difference = max(max1-min1, max2-min2)
        for i in range(n):
            A1.append(A[i]+i)
            A2.append(A[i]-i)
            if max1 is None:
                max1, max2, min1, min2 = A1[0], A2[0], A1[0], A2[0]
            else:
                max1 = max(A1[-1], max1)
                max2 = max(A2[-1], max2)
                min1 = min(A1[-1], min1)
                min2 = min(A2[-1], min2)
        max_abs_diff = max(max1-min1, max2-min2)
        return max_abs_diff

a = Solution()
inp = [1, 3, -1]
out = a.maxArr(inp)
print ('Max absolute Difference = ', out)

