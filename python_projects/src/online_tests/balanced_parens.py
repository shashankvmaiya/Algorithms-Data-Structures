'''
Created on Sep 18, 2018

@author: smaiya
'''
# Complete the code in this function. 

def balanced_parens(line):
    result = 'Y'
    paranthesis = ''
    stack = list()
    for char in line:
        if char == '(' or char =='{' or char == '[':
            stack.append(char)
            paranthesis = paranthesis+char
        if char == ')' or char =='}' or char == ']':
            paranthesis = paranthesis+char
            if stack: 
                last_paren = stack.pop()
                if char == ')' and last_paren != '(':
                    result = 'N'
                if char == '}' and last_paren != '{':
                    result = 'N'
                if char == ']' and last_paren != '[':
                    result = 'N'
            else:
                result = 'N'
    if stack:
        result = 'N'
    return result + ' ' + paranthesis

# Accept input from standard input
#line = input()
line = '2[3[4( 5 ) {34}]]'
line = '2[3[4( 5 ) {34)]]'
line = '2[3[4( 5 ) (34)]'
line = '2[3[4]( 5 ) (34)]'
print(balanced_parens(line))
