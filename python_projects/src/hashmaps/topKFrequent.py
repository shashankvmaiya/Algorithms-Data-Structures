'''
Q: Given a non-empty array of integers, return the k most frequent elements.
Solution O(n): 
    1. Obtain a hashmap of frequency of each element in the list
    2. Create another hashmap with frequency as the key and all the elements with that frequency as the value
    3. Starting from n (number of elements), get the elements from the hashmap created in 2. 

Created on Mar 17, 2019

@author: smaiya
'''
import collections

class Solution:
    def topKFrequent(self, nums, k):
        freq_list = {}
        for num in nums:
            freq_list[num] = freq_list.get(num, 0)+1
        
        num_list = collections.defaultdict(list)
        for num, freq in freq_list.items():
            num_list[freq].append(num)
        
        count = 0
        output = []
        for freq in range(len(nums), 0, -1):
            if freq in num_list:
                output+=num_list[freq]
                count+=len(num_list[freq])
                if count>=k:
                    break
        return output[:k]



inp = [1, 1, 1, 2, 2, 3]
out = Solution().topKFrequent(inp, 2)
print ('Top k frequent = ', out)