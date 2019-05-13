'''
Question: Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. 
All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. 
For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"]

Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]

Solution: Use DFS
    - Store the tickets in a graph, with the to city as the key and the destination cities and a boolean 
    to indicate if that ticket is used up as the value 
    - Call each child nodes by marking the boolean flag True. If it doesnt form a valid itinerary, then change 
    the boolean back to False 

Created on May 8, 2019

@author: smaiya
'''


class Solution:
    def findItinerary(self, tickets):
        
        graph = {}
        for t in tickets:
            if t[0] in graph:
                graph[t[0]].append([t[1], False])
            else:
                graph[t[0]] = [[t[1], False]]
        
        for city in graph:
            graph[city] = sorted(graph[city], key=lambda x: x[0])
        start = 'JFK'
        itinerary = [start]
        solution = []
        self.dfs(start, itinerary, graph, len(tickets)+1, solution)
        return solution[0]
        
    def dfs(self, city, itinerary, graph, length, solution):
        if len(itinerary)==length: # If itinerary contains all the ticket, then we found a solution
            solution.append(itinerary)
            return
        if city not in graph: # We are at a city where we cannot get out and we havent yet used up all the tickets
            return
        for index, dest in enumerate(graph[city]):
            if not graph[city][index][1]: # Over all tickets that havent been used up
                graph[city][index][1] = True # Set visited to True
                itinerary.append(dest[0]) # update current itinerary with the city 
                self.dfs(dest[0], itinerary, graph, length, solution)
                if solution:
                    return
                else: # The path doesnt lead to a solution
                    itinerary.pop() # Remove the city from itinerary
                    graph[city][index][1] = False # Set the visited to False
        return