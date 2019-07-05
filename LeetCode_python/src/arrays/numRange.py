class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def numRange(self, A, B, C):
        count = 0
        n = len(A)
        for i in range(n):
            curr_sum = A[i]
            count = count+1 if B<=curr_sum<=C else count
            if curr_sum>C:
                continue
            for j in range(i+1, n):
                curr_sum+=A[j]
                count = count+1 if B<=curr_sum<=C else count
                if curr_sum>C:
                    break
        return count


a = Solution()
(inp1, inp2, inp3) = ([10, 5, 1, 0, 2, 0, 6, 2], 6, 8)
#(inp1, inp2, inp3) = ([0,0,0,0,0], 0, 8)


str = a.numRange(inp1, inp2, inp3)
print ('Num Range: ', str)
