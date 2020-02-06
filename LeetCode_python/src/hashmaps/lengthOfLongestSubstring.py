'''
Q: Longest Substring Without Repeating Characters
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

Solution: Store the latest index of the character in a hasmap
If new letter is present in the hashmap, then update the start of substring. 
Update the max length and hashmap

Solution 2: Store the current sub string in hashmap and its index as value.
If new letter is present in the hashmap, then remove all the letters that came before that letter from the hashmap 
'''

class Solution:
    # @param A : string
    # @return an integer

    def lengthOfLongestSubstring(self, s):
        ans, start, n = 0, 0, len(s)
        map = dict()
        
        for i, char in enumerate(s):
            if char in map:
                start = max(start, map[char])
            ans = max(ans, i-start+1)
            map[char] = i+1
        return ans

    def lengthOfLongestSubstring_2(self, A):
        curr_len, max_len = 0, 0
        substring_char = dict()
        for i, char in enumerate(A):
            print (substring_char, char, curr_len, max_len)
            if char in substring_char:
                to_remove = A[i-curr_len:substring_char[char]]
                curr_len -= len(to_remove)
                for char_to_remove in to_remove:
                    if char_to_remove in substring_char:
                        del substring_char[char_to_remove]
            else:
                curr_len += 1
                max_len = curr_len if curr_len>max_len else max_len
            substring_char[char] = i
        return max_len



a = Solution()
inp = 'abcabcbb'
inp = 'bbbbbbb'
inp = 'abcbxysz'
inp = 'abcddaxybs'
inp = 'bbtablud'
#inp = '  '
#inp = 'aaaaaa cbd'
#inp = 'abcdefeabcds'
op = a.lengthOfLongestSubstring(inp)
print ('Length of Longest Substring = ', op)
