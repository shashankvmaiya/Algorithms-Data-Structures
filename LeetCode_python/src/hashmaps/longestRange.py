'''
# Uber Phone Interview 6/28/2018
Question: Unsorted array with unique numbers. What is the longest range
    Eg. [2, 1, 3, 5, 6, 9, 10] -> Longest range = 3 corresponding to [1, 2, 3], i.e. the continuous sequence of numbers

Solution: 
    - Use a Hashmap.
    - For each number as key, store start and end values of the interval it falls to 
    - Update the start and end every time a number is added to the interval

Better Solution:
    - Store all array elements in a hashmap
    - For all elements in the array arr[i]
        - Check if it is the starting point of an interval (or subsequence) by checking 
        if arr[i]-1 is present in the hash map
            - if true, then keep checking if arr[i]+1, 2.. are present in the hashmap and thereby 
            maintaining a the interval count 

'''
class Solution:
    # @param A : list of integers
    # @return an integer
    def longestRange(self, A):
        n = len(A)
        if n <= 1:
            return n
        numbers = dict()
        max_range = 0
        for num in A:
            if num not in numbers:
                start = numbers[num-1][0] if num-1 in numbers else num
                end = numbers[num+1][1] if num+1 in numbers else num
                numbers[start] = numbers[end] = numbers[num] = [start, end]
                curr_range = end-start+1
                max_range = curr_range if curr_range>max_range else max_range
        return max_range


a = Solution()
inp = [3, 2, 1, 0, 4, 6, 7, 8, 10]
inp = [1, 3, 6, 7, 2, 11, 13, 12, 5, 2, 3, 4]
str = a.longestRange(inp)
print ('Longest Range = ', str)
