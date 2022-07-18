'''
Q: Given a non-empty array of integers, return the k most frequent elements.
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Solution O(n): 
    1. Obtain a hashmap of frequency of each element in the list
    2. Create another hashmap with frequency as the key and all the elements with that frequency as the value
    3. Starting from n (number of elements), get the elements from the hashmap created in 2. 

Created on Mar 17, 2019

@author: smaiya
'''
import collections
import heapq
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
    
    def topKFrequent_heap(self, nums, k):
        heap = []
        freq = collections.Counter(nums) # Gives you unique nums as keys and the frequency as values
        for num in freq:
            temp = (freq[num], num)
            if len(heap)<k:
                heapq.heappush(heap, temp)
            else:
                heapq.heappushpop(heap, temp)
        
        result=[]   
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        
        return result[::-1]



inp = [1, 1, 1, 2, 2, 3]
out = Solution().topKFrequent(inp, 2)
print ('Top k frequent = ', out)