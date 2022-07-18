'''
2284. Sender With Largest Word Count

You have a chat log of n messages. You are given two string arrays messages and senders 
where messages[i] is a message sent by senders[i].

A message is list of words that are separated by a single space with no leading or 
trailing spaces. The word count of a sender is the total number of words sent by the sender. 
Note that a sender may send more than one message.

Return the sender with the largest word count. If there is more than one sender with the 
largest word count, return the one with the lexicographically largest name.

Note:

Uppercase letters come before lowercase letters in lexicographical order.
"Alice" and "alice" are distinct.
 

Example 1:

Input: messages = ["Hello userTwooo","Hi userThree","Wonderful day Alice","Nice day userThree"], 
senders = ["Alice","userTwo","userThree","Alice"]
Output: "Alice"
Explanation: Alice sends a total of 2 + 3 = 5 words.
userTwo sends a total of 2 words.
userThree sends a total of 3 words.
Since Alice has the largest word count, we return "Alice".

Solution:
    - Use a hashmap to store word count for each user

Created on July 10, 2022
@author: smaiya
'''
from typing import Dict, Any, List
from collections import defaultdict

class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        word_count_dict = defaultdict(int)
        max_wc, max_user = -1, ''
        for (m, s) in zip(messages, senders):
            word_count_dict[s]+=len(m.split())
            if word_count_dict[s]>max_wc or (word_count_dict[s]==max_wc and s>max_user):
                max_wc, max_user = word_count_dict[s], s
        
        return max_user

messages = ["Hello userTwooo","Hi userThree","Wonderful day Alice","Nice day userThree"]
senders = ["Alice","userTwo","userThree","Alice"]

ans = Solution().largestWordCount(messages, senders)
