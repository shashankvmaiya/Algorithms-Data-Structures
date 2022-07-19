'''
Created on Jul 7, 2018
A positive number N
Heights : A list of heights of N persons standing in a queue
Infronts : A list of numbers corresponding to each person (P) that gives the number of
persons who are taller than P and standing in front of P

You need to return list of actual order of persons height
Input : 
Heights: 5 3 2 6 1 4
InFronts: 0 1 2 0 3 2

actual order is: 5 3 2 1 6 4 
@author: smaiya
'''

class Person:
    def __init__(self, height, in_front):
        self.height = height
        self.in_front = in_front
        
class IntervalTree:
    def __init__(self, person):
        self.person = person
        self.left = None
        self.right = None
        self.val = 1
        

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    
    def insert(self, root, person, val):
        if val<root.val:
            if root.left is None:
                root.left = IntervalTree(person)
            else:
                self.insert(root.left, person, val)
            root.val+=1
        else:
            if root.right is None:
                root.right = IntervalTree(person)
            else:
                self.insert(root.right, person, val-root.val)
                
    def in_order(self, root):
        if root is None:
            return None
        stack = []
        node = root
        inOrderList = []
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                inOrderList.append(node.person.height)
                node = node.right
        return inOrderList
                
    
    def order(self, A, B):
        persons = [None]*len(A)
        for i in range(len(A)):
            persons[i] = Person(A[i], B[i])
        persons.sort(key=lambda x: x.height, reverse=True)
        root = IntervalTree(persons[0])
        for i in range(1, len(persons)):
            self.insert(root, persons[i], persons[i].in_front)
        
        result = self.in_order(root)
        return result


a = Solution()
heights = [5, 3, 2, 6, 1, 4]
infronts = [0, 1, 2, 0, 3, 2]
order = a.order(heights, infronts)
print ('Actual Order = ', order)

