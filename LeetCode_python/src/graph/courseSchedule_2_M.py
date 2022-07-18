'''
210. Course Schedule II

Question: 
There are a total of n courses you have to take, labeled from 0 to n-1
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.
If it is impossible to finish all courses, return an empty array.
 
Solution: 
    - Use stack or queues to store the courses that can be taken at any time
    - Every time a course is taken, reduce the in_degree of all nodes that depend on the course that was taken
    - If the in_degree of the course = 0, then there is no dependency and can be taken. Hence push it to the stack

Created on Apr 21, 2019

@author: smaiya
'''


class Solution:
    def findOrder(self, numCourses, prerequisites):
        
        in_degree = {}
        course_order = {}
        
        for pair in prerequisites: 
            in_degree[pair[0]] = in_degree.get(pair[0], 0)+1
            if pair[1] in course_order:
                course_order[pair[1]].append(pair[0])
            else:
                course_order[pair[1]] = [pair[0]]
        
        stack = []    
        for course in range(numCourses):
            if course not in in_degree:
                stack.append(course)
        result = []
        while stack:
            course = stack.pop()
            result.append(course)
            if course in course_order: 
                for c in course_order[course]:
                    in_degree[c]-=1
                    if in_degree[c]==0:
                        stack.append(c)
        if len(result)<numCourses:
            return []
        else: 
            return result
        
        