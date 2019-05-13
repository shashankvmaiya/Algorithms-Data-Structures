'''
Question: A message containing letters from A-Z is being encoded to numbers using the following mapping:
'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.
Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Solution: Dynamic Programming
    - D(n) = Number of ways to decode using n numbers
    - D(n) = D1(n) + D2(n) where
        - D1(n) = Number of ways to decode with n-th number as a 1-digit number
        - D2(n) = Number of ways to decode with n-th number as a 2-digit number
    - D1(n) = D(n-1) if num(n) !=0 else 0
    - D2(n) = D(n-2) if num(n-1, n) lies between 10 and 26

Created on Apr 7, 2019

@author: smaiya
'''

class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        if len(s)==1:
            return 1 if s[0]!='0' else 0
        n = len(s)
        
        # 1-indexing instead of 0-indexing. 0-th index used for initialization
        dp = [0 for i in range(n+1)]
        
        dp[0]=1 # Initialization constant
        dp[1]=1 if s[0]!='0' else 0 # Corresponds to the first letter
        for i in range(2, n+1):
            one_digit = int(s[i-1:i]) 
            two_digit = int(s[i-2:i])
            # Number of codes using ith number as 1-digit is only possible if it is not a 0
            if one_digit!=0:
                dp[i] += dp[i-1]
            if two_digit>=10 and two_digit<=26:
                dp[i] += dp[i-2]
                
        return dp[-1]
    