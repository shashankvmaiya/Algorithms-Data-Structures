'''
Question: Number of inversions (swaps) required to make the array sorted
E.g., Input: [2, 4, 1, 3, 5] Output = 3

Solution: Dynamic Programming. O(nlogn) for sorting
    - D(n) = D(n-1) + x
    where D(n) = number of swaps required to make the first n array sorted
    x = number of elements in the (n-1) elements that are greater than x
    - Maintain a sorted array of (n-1). Inserting the n-th element = O(log n)
'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def countInversions(self, A):
        n = len(A)
        A_sorted = [];
        num_inversions = 0
        A_sorted.append(A[0])
        for idx in range(1, n):
            num_inversions += len([1 for i in A_sorted if i>A[idx]])    # Can be optimized to run in log N using Binary Search
            A_sorted.append(A[idx])
            A_sorted.sort()
        return num_inversions


a = Solution()
#inp = [3, 2, 1, 0, 4, 6, 7, 8, 10]
#inp = [1, 3, 6, 7, 2, 11, 13, 12, 5, 2, 3, 4]
inp = [2, 4, 1, 3, 5]
#inp = [2, 1, 1, 1, 1]
str = a.countInversions(inp)
print ('Number of Inversions = ', str)
