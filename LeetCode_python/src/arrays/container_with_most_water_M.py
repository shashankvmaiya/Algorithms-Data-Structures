'''
11. Container With Most Water

Question: https://leetcode.com/problems/container-with-most-water/
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
Input: [1,8,6,2,5,4,8,3,7]
Output: 49

Solution: 
    - 2 pointer approach - one starting from the beginning and the other from the end
    - Since height is limited by the minimum heights of the 2 sides, adjust the pointer which corresponds to the minimum height

Created on Jun 1, 2019

@author: smaiya
'''

class Solution:
    def maxArea(self, height):
        max_area = 0
        l, r = 0, len(height)-1
        while(l<r):
            max_area = max(max_area, min(height[l], height[r])*(r-l))
            if height[r]>height[l]:
                l+=1
            else:
                r-=1
        return max_area
    
    