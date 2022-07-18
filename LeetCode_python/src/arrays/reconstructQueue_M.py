'''
406. Queue Reconstruction by Height

You are given an array of people, people, which are the attributes of some people in a queue 
(not necessarily in order). Each people[i] = [hi, ki] represents the ith person of height hi 
with exactly ki other people in front who have a height greater than or equal to hi.

Reconstruct and return the queue that is represented by the input array people. The returned 
queue should be formatted as an array queue, where queue[j] = [hj, kj] is the attributes of 
the jth person in the queue (queue[0] is the person at the front of the queue).

Input: people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
Output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]

Input: people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
Output: [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]

Solution:
    - Sort the people first, decreasing based on height and second based on number of people in front
    [[7,0],[7,1],[6,1],[5,0],[5,2],[4,4]]
    - Start by inserting the tallest person into the position determined by number of people in front
    - Inserting will push the remaining taller people to the right
    - SInce the remaining people to be inserted are only shorter, it wouldnt impact even if they are inserted 
    in front of the current person
    
input: [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
sort: [[7,0], [7,1], [6,1], [5,0], [5,2], [4,4]]
step1: [[7,0]]
step2: [[7,0], [7,1]]
step3: [[7,0], [6,1], [7,1]]
step4: [[5,0], [7,0], [6,1], [7,1]]
step5: [[5,0], [7,0], [5,2], [6,1], [7,1]]
step6: [[5,0], [7,0], [5,2], [4,4], [6,1], [7,1]]

'''

class Solution:
    def reconstructQueue(self, people):
        people.sort(key=lambda x: (-x[0], x[1]))
        result = []
        for p in people:
            result.insert(p[1], p)
        return result