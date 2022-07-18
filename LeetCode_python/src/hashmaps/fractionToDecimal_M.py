'''
Q: Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
If the fractional part is repeating, enclose the repeating part in parentheses.
Input: numerator = 2, denominator = 3
Output: "0.(6)"

Solution: 
    Store the remainders as keys in a hashmap and the index as values
    Decimals will start to repeat once the remainders repeat. 
    Index stored as values in the hashmap indicates the starting point of the recurring decimals
    
Created on Mar 17, 2019

@author: smaiya
'''
class Solution:
    def fractionToDecimal(self, numerator, denominator):
        if numerator==0:
            return '0'
        sign='' if numerator*denominator>0 else '-'
        numerator, denominator=abs(numerator), abs(denominator)
        quotient = (numerator//denominator)
        if numerator%denominator==0:
            return sign+str(quotient)
        numerator-=quotient*denominator
        
        remainder = {}
        decimal = ''
        idx=0
        while numerator!=0:
            curr_quot = 10*numerator//denominator
            
            if numerator in remainder:
                decimal = decimal[:remainder[numerator]]+'('+decimal[remainder[numerator]:]+')'
                break
            else:
                decimal+=str(curr_quot)
                if numerator==0:
                    break
                remainder[numerator] = idx
                idx+=1
            numerator = 10*numerator%denominator
        return sign+str(quotient)+'.'+decimal


#out = Solution().fractionToDecimal(1,6)
#out = Solution().fractionToDecimal(2,7)
#out = Solution().fractionToDecimal(2,1)
#out = Solution().fractionToDecimal(1,2)
#out = Solution().fractionToDecimal(-50,8)
out = Solution().fractionToDecimal(-2147483648,1)
print ('Fraction to Decimal = ', out)