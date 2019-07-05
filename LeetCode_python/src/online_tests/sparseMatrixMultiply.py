'''
Created on Apr 8, 2019

@author: smaiya
'''

"""
logistic regression
 objective: argmin (beta) (sum_i(sum_j(xij*betas_j) - yi)^2)
 d/dbeta_j(loss function) = 0
 yi
 xis for each data bit
 sum(xi^2*beta_i) beta_1 proporational to the snr_i
  pilot bits -- known bits sent by network and known power
  using these pilot bits...we estimate the snr_i
"""

"""
Given two sparse matrices A and B, return the result of multiplication of A and B.
You may assume that A's column number is equal to B's row number.
A = mxn -- ~x elements x<<mxn
B = nxp -- ~y elements y<<nxp
Multiplication ~ O(x+y)
"""
#Operations(rawA, rawB).multiply() 

class Operations(object):
    def __init__(self, rawA, rawB):
        self.sparseA = self.sparse_matrix(rawA)
        self.sparseB = self.sparse_matrix(rawB)
        self.m = len(rawA)
        self.n = len(rawA[0])
        self.p = len(rawB[0])

    def sparse_matrix(self, matrix):
        sparse_matrix = {}
        num_cols = len(matrix[0])
        for row_idx, row in enumerate(matrix):
            for col_idx, element in enumerate(row):
                if (element!=0):
                    sparse_matrix[col_idx+row_idx*num_cols] = element
        return sparse_matrix

    def multiply(self):
        output = {}
        for i in range(self.m):
            for j in range(self.p):
                # mth row of sparseA and pth column of sparseB
                for k in range(self.n):
                    mult_cell = 0
                    if (self.sparseA[k+i*self.n] and self.sparseB[j+k*self.n]): 
                        mult_cell+= (self.sparseA[k+i*self.n] * self.sparseB[j+k*self.n])
                if mult_cell!=0:
                    output[j+i*self.m] = mult_cell

        for idxA, valA in self.sparseA.items():
            
            for idxB, valB in self.sparseB.items():
                for k in range(self.n):
                    mult_cell = 0
                    # Check if idxA and idxB are applicable to k
                    if (idxA):
                        mult_cell+=valA*valB


        return output