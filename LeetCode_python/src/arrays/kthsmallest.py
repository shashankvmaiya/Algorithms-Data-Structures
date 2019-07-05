class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, B):
        sort_a = sorted(A)
        return sort_a[B-1]

a = Solution()
(inp1, inp2) = ([2, 1, 4, 3, 2], 3)


str = a.kthsmallest(inp1, inp2)
print ('kth Smallest: ', str)
