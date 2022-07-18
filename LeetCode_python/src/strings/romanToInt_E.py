'''
13. Roman to Integer

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
Given a roman numeral, convert it to an integer.

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

'''
class Solution:
    # @param A : string
    # @return an integer
    def romanToInt(self, A):
        roman_to_int = dict()
        roman_to_int['I'] = 1
        roman_to_int['V'] = 5
        roman_to_int['X'] = 10
        roman_to_int['L'] = 50
        roman_to_int['C'] = 100
        roman_to_int['D'] = 500
        roman_to_int['M'] = 1000

        n = len(A)
        if n == 0:
            return 0
        curr_max = 0
        output = 0
        for i in range(n-1,-1,-1):
            if A[i] in roman_to_int:
                curr_int_value = roman_to_int[A[i]]
                if curr_int_value>=curr_max:
                    output += curr_int_value
                    curr_max = curr_int_value
                else:
                    output -= curr_int_value
                #print (curr_int_value, curr_max, output)
            else:
                return 'Invalid Roman Number'
        return output

a = Solution()
inp = 'MCMLIV'
str = a.romanToInt(inp)
print ('Integer Value = ', str)
