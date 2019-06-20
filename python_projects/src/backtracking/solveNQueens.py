'''
Question: https://leetcode.com/problems/n-queens/
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' 
both indicate a queen and an empty space respectively.
Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.

Created on Jul 12, 2018

@author: smaiya
'''
import copy
class Solution:
    # @param A : integer
    # @return a list of list of strings
    def __init__(self):
        self.solutions = []
    def is_safe(self, board, row, col, size):
        # Check for column
        if 1 in board[row][:]:
            return False
        
        # Check for left diagonal
        x, y = row, col
        while x<size and y>=0:
            if board[x][y] == 1:
                return False
            x+=1
            y-=1
            
        # Check for right diagonal
        x, y = row, col
        while x>=0 and y>=0:
            if board[x][y] == 1:
                return False
            x-=1
            y-=1
        return True
    
    def solve(self, board, col, size):
        if col>=size:
            return
        for row in range(size):
            if self.is_safe(board, row, col, size):
                board[row][col] = 1
                if col == size-1:
                    self.add_solution(board)
                    board[row][col] = 0
                    return
                self.solve(board, col+1, size)
                board[row][col] = 0
                
    def add_solution(self, board):
        temp = copy.deepcopy(board)
        self.solutions.append(temp)
    
    
    
    def solveNQueens(self, A):
        board = [[0]*A for x in range(A)]
        self.solve(board, 0, A)
        str_solution = []
        for sol in self.solutions:
            str_board = []
            for row in range(A):
                index = sol[row].index(1)
                str_row = ''.join(['.']*index + ['Q']+ ['.']*(A-index-1))
                str_board.append(str_row)
            str_solution.append(str_board)
        return str_solution


a = Solution()
n=4
out = a.solveNQueens(n)
print('N Queen solution = ', out)

