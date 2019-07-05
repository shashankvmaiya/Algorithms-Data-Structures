'''
Question: Find the next permuation of a list of number
E.g. Input: [3, 9, 4, 2, 1]
Output: [4, 1, 2, 3, 9]

Solution: 
1. Check for max i such that A[i] < A[i+1]
2. Swap(A[i], next highest number such that j>i)
3. Sort A[i+1:] = same as A[i+1].reverse() (since all numbers from i was in decreasing order prior to swap) 

'''


class Solution:
    # @param A : list of integers
    # @return the same list of integer after modification
    def nextPermutation(self, A):
        n = len(A)
        if n <= 1:
            return A
        swap_idx=None
        # Check for max i s.t. A[i]<A[i+1]
        for i in range(0, n-1):
            if A[i]<A[i+1]:
                swap_idx = i
        # If already in decreasing order, then return increasing order of A
        if swap_idx is None:
            A.reverse()
            return A
        # Next highest number from i+1 to n-1
        next_highest = swap_idx+1
        for j in range(swap_idx+1, n):
            if A[j] > A[swap_idx] and A[j] < A[next_highest]:
                next_highest = j
        #print(swap_idx, next_highest)
        (A[swap_idx], A[next_highest]) = (A[next_highest], A[swap_idx])
        b_temp = A[swap_idx+1:]
        b_temp.reverse()
        #print(A[:swap_idx+1], b_temp)
        A_next = A[:swap_idx+1] + b_temp

        return A_next



a = Solution()
inp = [3, 9, 4, 2, 1]
#inp = [4, 9, 3, 2, 1]
#inp = [1, 9, 1, 2, 1]
str = a.nextPermutation(inp)
print ('Next Permutation = ', str)
