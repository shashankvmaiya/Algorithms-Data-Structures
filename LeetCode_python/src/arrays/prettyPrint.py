class Solution:
    # @param A : integer
    # @return a list of list of integers
    def prettyPrint(self, A):
        output = list()
        for idx in range(A):
            temp = list(range(A, A-idx-1, -1)) + [A-idx]*(A-idx-1)
            curr_list = temp + temp[-2::-1]
            output.append(curr_list)
        for idx in range(A-2,-1,-1):
            output.append(output[idx])
        return output

a = Solution()
inp = 1
str = a.prettyPrint(inp)
print ('Pretty Print: ', str)
