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
