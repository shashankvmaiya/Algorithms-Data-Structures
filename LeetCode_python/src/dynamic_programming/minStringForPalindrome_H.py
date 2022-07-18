'''
1312. Minimum Insertion Steps to Make a String Palindrome

Question: Minimum number of characters to make a string a palindrome provided it can be inserted 
anywhere in between the string
Eg: Input = 'xybbayx'
Output = 1 since a can be inserted between y and b to make it a palindrome

Solution: Dynamic Programming O(n^2)
    - Populate min_count[i, j] array containing the minimum number of characters required to make Si to Sj a palindrome
    - Output = min_count[0, n-1]
    - Start populating from length 1 to length n
    Method to populate min_count[i, j]
        min_count[i, j] = min_count[i+1, j-1] if Si == Sj
        min_count[i, j] = min (min_count[i+1, j], min_count[i, j-1]) + 1 if Si != Sj
'''

class Solution:
    # @param A : string
    # @return an integer
    def minInsertions(self, A):
        n = len(A)
        if n==1:
            return 0
        elif n==2:
            if A[0]==A[1]:
                return 0
            else:
                return 1

        min_count = [[0]*n for i in range(n)]
        for i in range(n-1):
            if A[i]==A[i+1]:
                min_count[i][i+1] = 0
            else:
                min_count[i][i+1] = 1

        for length in range(3, n+1):
            for i in range(n-length+1):
                if A[i] == A[i+length-1]:
                    min_count[i][i+length-1] = min_count[i+1][i+length-2]
                else:
                    min_count[i][i+length-1] = 1 + min(min_count[i+1][i+length-1], min_count[i][i+length-2])

        #print(min_count)
        return min_count[0][n-1]

a = Solution()
inp = 'hqghumeaylnlfdxfi'
inp = 'xybbayx'
str = a.minInsertions(inp)
print ('Minimum length of string for Palindrome = ', str)
