'''
The appeal of a string is the number of distinct characters found in the string.

For example, the appeal of "abbca" is 3 because it has 3 distinct characters: 'a', 'b', and 'c'.
Given a string s, return the total appeal of all of its substrings.

A substring is a contiguous sequence of characters within a string.


Input: s = "abbca"
Output: 28
Explanation: The following are the substrings of "abbca":
- Substrings of length 1: "a", "b", "b", "c", "a" have an appeal of 1, 1, 1, 1, and 1 respectively. The sum is 5.
- Substrings of length 2: "ab", "bb", "bc", "ca" have an appeal of 2, 1, 2, and 2 respectively. The sum is 7.
- Substrings of length 3: "abb", "bbc", "bca" have an appeal of 2, 2, and 3 respectively. The sum is 7.
- Substrings of length 4: "abbc", "bbca" have an appeal of 3 and 3 respectively. The sum is 6.
- Substrings of length 5: "abbca" has an appeal of 3. The sum is 3.
The total sum is 5 + 7 + 7 + 6 + 3 = 28.


Solution:
    - Store the previously seen characters's index in a hashmap
    - For each newly added character, we find the appeal that it is brining in and add that into the result
    - If the newly added character at i is not present before, 
        - then appeal it is bringing in = appeal(i-1) + (i+1)
    - If the newly added character at i is present before, 
        - then the appeal it is bringing in = appeal(i-1) + (i-idx of where it was last seen)

Created on July 10, 2022
@author: smaiya
'''
from typing import Dict, Any, List
from collections import defaultdict

class Solution:
    def appealSum(self, s: str) -> int:
        dp = []
        prev_char_idx = {}
        result, prev, curr = 0, 0, 0
        for i, c in enumerate(s):
            # curr = appeal due to addition of character c at i
            if c in prev_char_idx:
                curr = prev + i - prev_char_idx[c]
            else:
                curr = prev + i + 1
            # result = sum of all the appeal up to i
            result+=curr
            prev = curr
            prev_char_idx[c]=i
        return result



s = "abbca"
ans = Solution().appealSum(s)
