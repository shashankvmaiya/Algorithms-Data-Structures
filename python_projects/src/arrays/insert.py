'''
Created on Jul 2, 2018
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
@author: smaiya
'''

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, new_interval):
        merged_intervals = list()
        if new_interval.start > new_interval.end:
            new_interval.start, new_interval.end = new_interval.end, new_interval.start
        if intervals == []:
            merged_intervals.append(new_interval)
            return merged_intervals
        n = len(intervals)
        if new_interval.start>= intervals[n-1].start:
            intervals.insert(n, new_interval)
        else:
            for i in range(n):
                if intervals[i].start>new_interval.start:
                    intervals.insert(i, new_interval)
        first = True
        for interval in intervals:
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
#inp.append(Interval(1, 3))
#inp.append(Interval(6, 9))
#inp2 = Interval(2, 5)

#inp.append(Interval(1, 2))
#inp.append(Interval(3, 5))
#inp.append(Interval(6, 7))
#inp.append(Interval(8, 10))
#inp.append(Interval(12, 16))
#inp2 = Interval(4, 9)

#inp2 = Interval(1, 1)

inp.append(Interval(1, 2))
inp.append(Interval(3, 6))
inp2 = Interval(10, 8)

out = a.insert(inp, inp2)
print('Merged Invervals: ')
for interval in out:
    print ('[', interval.start, interval.end, ']')
