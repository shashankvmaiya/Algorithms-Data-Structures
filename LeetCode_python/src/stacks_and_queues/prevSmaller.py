'''
Created on Jun 30, 2018
Given an array, find the nearest smaller element G[i] for every element A[i] in the array 
such that the element has an index smaller than i.
Input : A : [4, 5, 2, 10, 8]
Return : [-1, 4, -1, 2, 2]
Input : A : [3, 2, 1]
Return : [-1, -1, -1]
@author: smaiya
'''

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, A):
        n = len(A)
        prev_smaller = None
        for i in range(n):
            # Initialize the first element as -1
            if prev_smaller is None:
                prev_smaller = [-1]
            else:
                # If previous element is smaller, then prev_smaller[i] = A[i-1]
                if A[i] > A[i-1]:
                    prev_smaller.append(A[i-1])
                else:
                    # Else, search in the prev_smaller list for the next smaller element 
                    count = i-1
                    while prev_smaller[count] != -1 and prev_smaller[count]>=A[i]:
                        count-=1
                    prev_smaller.append(prev_smaller[count])
        return prev_smaller

a = Solution()
inp = [4, 5, 2, 10, 8]
inp = [3, 2, 1]
inp = [4, 2, 1, 7, 6, 8, 7, 5]
inp = [7, 1, 4, 8, 3, 2, 5, 9, 8]
inp = [1, 1, 1, 1]
inp = [8, 23, 22, 16, 22, 7, 7, 27, 35, 27, 32, 20, 5, 1, 35, 28, 20, 6, 16, 26, 48, 34 ]
out = a.prevSmaller(inp)
print ('Nearest Smaller Element = ', out)

