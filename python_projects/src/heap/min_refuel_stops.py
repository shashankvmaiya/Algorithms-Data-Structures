'''
Question: A car travels from a starting position to a destination which is target miles east of the starting position.

Along the way, there are gas stations.  Each station[i] represents a gas station that is station[i][0] miles east of the 
starting position, and has station[i][1] liters of gas.

The car starts with an infinite tank of gas, which initially has startFuel liters of fuel in it.  
It uses 1 liter of gas per 1 mile that it drives.When the car reaches a gas station, it may stop and refuel, transferring all 
the gas from the station into the car.

What is the least number of refueling stops the car must make in order to reach its destination?  
If it cannot reach the destination, return -1.

Solution: 
    - When driving past a gas station, store all the fuel capacity. 
    - Upon running out of fuel, fill from the the largest gas station that we have passed 
    - Use max_heap to store the fueling capacity of each station that we pass
    - Keep track of the the 'tank', the current fuel. Once we reach a station but have negative fuel, 
    add capacities of the largest gas stations that we have driven past until the tank is > 0
    - If this process fails, then retun -1 

Created on May 27, 2019

@author: smaiya
'''

import heapq

class Solution:
    def minRefuelStops(self, target, startFuel, stations):
        max_heap = []
        stations.append([target, float('Inf')]) # Adding the target station that we have to drive to
        
        stops = 0 # Number of station stops for refueling
        prev = 0 
        tank = startFuel
        for location, fuel in stations:
            tank -= (location-prev) # Each station, update the tank (current fuel content)
            while tank<0 and max_heap: # If we run out of fuel, fill starting from the largest gas station that we have passed
                tank+=-heapq.heappop(max_heap)
                stops+=1
            if tank<0: # Inspite of refueling from all gas stations we have passed by, if we still have <0 tank then return -1
                return -1
            heapq.heappush(max_heap, -fuel) # Store the station capacity in a max_heap that we are passing by
            prev = location
            
        return stops
