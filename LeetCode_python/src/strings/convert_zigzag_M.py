'''
6. Zigzag Conversion

Question: The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
(you may want to display this pattern in a fixed font for better legibility)
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Solution: 
    - Obtain the substring for each row and concatenate
    - For the first and the last row, substring = s[i::2*(numRows-1)]
    - For the intermediate rows, there are 2 contributions (with length of the first substring >= second)
        - s[i::2*(numRows-1)]  --> Downward path
        - s[2*numRows-i-2::2*(numRows-1)] --> Upward path

Created on Apr 5, 2019

@author: smaiya
'''



class Solution:
    def convert(self, s, numRows):
        if numRows==1:
            return s
        if numRows==2:
            s1 = s[::2]
            s2 = s[1::2]
            return (s1+s2)
        
        zig_zag_string = ''
        for i in range(numRows):
            if i==0 or i==(numRows-1):
                curr_row_str = s[i::2*(numRows-1)]
            else:
                s1 = s[i::2*(numRows-1)]
                s2 = s[2*numRows-i-2::2*(numRows-1)]
                curr_row_str = [c1+c2 for c1, c2 in zip(s1, s2)]
                curr_row_str += list(s1[len(s2):])
                curr_row_str = ''.join(curr_row_str)
            zig_zag_string += curr_row_str
        return zig_zag_string
    
    
inp = 'PAYPALISHIRING'
op = Solution().convert(inp, 3)
print ('Zig Zag string = ', op)
