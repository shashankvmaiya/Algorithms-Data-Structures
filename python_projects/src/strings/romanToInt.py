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
