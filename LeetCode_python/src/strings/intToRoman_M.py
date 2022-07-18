'''
12. Integer to Roman
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, 
which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral
 for four is not IIII. Instead, the number four is written as IV. Because the one is before the 
 five we subtract it making four. The same principle applies to the number nine, which is written 
 as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.

Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

'''
class Solution:
    # @param A : integer
    # @return a strings
    def intToRoman(self, A):
        roman_output = ''
        remainder = A
        # Thousands
        thousands = int(remainder/1000)
        remainder = remainder - thousands*1000
        roman_output = roman_output + 'M'*thousands
        # Hundreds
        hundreds = int(remainder/100)
        remainder = remainder - hundreds*100
        roman_output = roman_output + self.digit_to_roman(hundreds, 'M', 'D', 'C')
        # Tens
        tens = int(remainder/10)
        remainder = remainder - tens*10
        roman_output = roman_output + self.digit_to_roman(tens, 'C', 'L', 'X')
        # Units
        units = int(remainder/1)
        remainder = remainder - units*1
        roman_output = roman_output + self.digit_to_roman(units, 'X', 'V', 'I')

        return roman_output

    def digit_to_roman(self, digit, high, mid, low):
        if digit == 9:
            roman = low+high
        elif digit >=5:
            roman = mid+low*(digit-5)
        elif digit ==4:
            roman = low+mid
        elif digit >=1:
            roman = low*digit
        else:
            roman = ''
        return roman


a = Solution()
inp = 1
str = a.intToRoman(inp)
print ('Roman Value = ', str)
