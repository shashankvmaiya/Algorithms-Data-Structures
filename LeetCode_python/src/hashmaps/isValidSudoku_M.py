'''
Q: Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated 
according to the following rules:

- Each row must contain the digits 1-9 without repetition.
- Each column must contain the digits 1-9 without repetition.
- Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note: 
- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
- Only the filled cells need to be validated according to the mentioned rules.

Solution: Use 3 x 9 dictionaries - for each row, column and box. If same number repeats in 
any of the dict, then invalid 
'''

class Solution:
    # @param A : tuple of strings
    # @return an integer
    def isValidSudoku(self, A):
        row_dict_list = [dict() for x in range(9)]
        col_dict_list = [dict() for x in range(9)]
        box_dict_list = [dict() for x in range(9)]
        for row_idx in range(9):
            for col_idx in range(9):
                value = A[row_idx][col_idx]
                if value.isdigit():
                    box_idx = int(row_idx/3)*3 + int(col_idx/3)
                    if value in row_dict_list[row_idx] or value in col_dict_list[col_idx] or value in box_dict_list[box_idx]:
                        #print (value, row_idx, col_idx, box_idx)
                        return 0
                    row_dict_list[row_idx][value] = 1
                    col_dict_list[col_idx][value] = 1
                    box_dict_list[box_idx][value] = 1
        #print (box_dict_list)
        return 1


a = Solution()
inp = [ "....5..1.", ".4.3.....", ".....3..1", "8......2.", "..2.7....", ".15......", ".....2...", ".2.9.....", "..4......" ]
for i in inp:
    print(i)
str = a.isValidSudoku(inp)
print ('Valid Sudoku = ', str)
