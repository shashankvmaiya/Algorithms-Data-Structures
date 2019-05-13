'''
Question: Given a collection of intervals, merge all overlapping intervals.
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18]

Solution: 
    - Sort the interval based on the interval start
    - Starting from the first interval, keep checking if it overlaps with the following intervals
    and merge them. 
    - Add the merged interval to the output list the moment an interval doesnt overlap with 
    the current merged interval 
    - If interval i doesnt overlap with i-1, then i+1 doesnt overlap either
    

Created on Jun 30, 2018

@author: smaiya
'''

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
        

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        sorted_intervals = sorted(intervals, key=lambda interval:interval.start, reverse=False)
        merged_intervals = list()
        
        first = True
        for interval in sorted_intervals:
            if first:
                curr_start, curr_end, first = interval.start, interval.end, False
                continue
            if interval.start <= curr_end:
                curr_end = interval.end if interval.end>curr_end else curr_end
            else:
                new_interval = Interval(curr_start, curr_end)
                merged_intervals.append(new_interval)
                curr_start, curr_end = interval.start, interval.end
        new_interval = Interval(curr_start, curr_end)
        merged_intervals.append(new_interval)
        return merged_intervals


a = Solution()
inp = list()
inp.append(Interval(1, 3))
inp.append(Interval(2, 7))
inp.append(Interval(3, 5))
inp.append(Interval(1, 2))
inp.append(Interval(9, 10))
inp.append(Interval(12, 16))
inp.append(Interval(13, 15))
inp.append(Interval(12, 14))
inp.append(Interval(21, 22))

out = a.merge(inp)
print('Merged Invervals: ')
for interval in out:
    print ('[', interval.start, interval.end, ']')

