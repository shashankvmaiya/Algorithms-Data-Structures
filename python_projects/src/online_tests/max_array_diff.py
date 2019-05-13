'''
Created on Sep 18, 2018

@author: smaiya
'''


# Complete the code in this function. 
# Return the absolute value of the largest difference between any two numbers on the line

def max_array_diff(phrase):
    inp_num = [int(i) for i in phrase.split()]
    return max(inp_num)-min(inp_num)

# Accept input from standard input
phrase = input()
#phrase = [1, 9, 2, 7, 10, 4, 3]
print(max_array_diff(phrase))
