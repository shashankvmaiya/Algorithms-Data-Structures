'''
567. Permutation in String

Question: Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. 
In other words, one of the first string's permutations is the substring of the second string.
Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").

Input:s1= "ab" s2 = "eidboaoo"
Output: False

Solution: 
    - Two pointers approach
    - Create a hashmap containing count of each letter
    - From n_s1 to n_s2, use a moving window approach
        - increment the added character and decrement the excluded character
    - Check if the counts of each character in s1 hashmap is the same 
Created on Apr 14, 2019

@author: smaiya
'''


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n_s1, n_s2 = len(s1), len(s2)
        if n_s1>n_s2:
            return False
        # Maintain the counts of each character in the strings
        map_s1, map_s2 = {}, {}
        for i in range(n_s1):
            map_s1[s1[i]] = map_s1.get(s1[i], 0)+1
            map_s2[s2[i]] = map_s2.get(s2[i], 0)+1
        
        # If hashmaps are identical, then return true
        if map_s1==map_s2:
            return True
        
        for i in range(n_s1, n_s2):
            # Add the ith character and remove the i-n_s1 th character from s2 hashmap
            map_s2[s2[i]] = map_s2.get(s2[i], 0)+1
            map_s2[s2[i-n_s1]] = map_s2.get(s2[i-n_s1], 0)-1
            
            # Check if the counts of the s1 and s2 hashmap are the same 
            # Note that the hashmaps are different since many character counts in s2 = 0
            match = True
            for char, count in map_s1.items():
                if map_s2.get(char)!=count:
                    match = False
                    break
            if match:
                return True
        return False