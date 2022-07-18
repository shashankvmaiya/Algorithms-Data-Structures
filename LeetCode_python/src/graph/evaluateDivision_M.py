'''
399. Evaluate Division

Question: Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). 
Given some queries, return the answers. If the answer does not exist, return -1.0

Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

Solution: 
    - Store the equations as a graph. 
        - Each node connected to its denominator with the quotient stored as the value
        - For each a/b, also store b/a
        - Additionally store a self loop to check for a/a = 1
    - To get the answer for the query, start with the numerator and do a breadth first search till you reach the denominator (keeping track of visited nodes)
    - Store the cumulative product and push it to the queue along with the node

Created on May 7, 2019

@author: smaiya
'''


class Solution:
    def calcEquation(self, equations, values, queries):
        
        # Create the division table
        table = {}
        for eq, val in zip(equations, values): 
            num, den, ans = eq[0], eq[1], val
            # Storing a/b
            if num in table:
                table[num].append([den, ans])
            else:
                table[num] = [[den, ans]]
            
            # Storing b/a
            if den in table:
                table[den].append([num, 1/ans])
            else:
                table[den] = [[num, 1/ans]]
        
        # Storing a/a
        for var in table:
            table[var].append([var, 1.0])
                
        solution = [-1 for i in range(len(queries))]
        for idx, q in enumerate(queries):
            visited = {}
            # Eliminating x/x queries if x is not provided among the equations
            if q[0] not in table:
                continue
            queue = [[q[0], 1.0]]
            while queue:
                node, val = queue.pop(0)
                visited[node]=1
                if node==q[1]:
                    solution[idx]=val
                    break
                for den, quotient in table[node]:
                    if den not in visited:
                        queue.append([den, val*quotient])
        return solution