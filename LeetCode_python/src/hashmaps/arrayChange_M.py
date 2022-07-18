'''
2295. Replace Elements in an Array

You are given a 0-indexed array nums that consists of n distinct positive integers. 
Apply m operations to this array, where in the ith operation you replace the number 
operations[i][0] with operations[i][1].

It is guaranteed that in the ith operation:

operations[i][0] exists in nums.
operations[i][1] does not exist in nums.
Return the array obtained after applying all the operations.

Input: nums = [1,2,4,6], operations = [[1,3],[4,7],[6,1]]
Output: [3,2,7,1]
Explanation: We perform the following operations on nums:
- Replace the number 1 with 3. nums becomes [3,2,4,6].
- Replace the number 4 with 7. nums becomes [3,2,7,6].
- Replace the number 6 with 1. nums becomes [3,2,7,1].
We return the final array [3,2,7,1].

Input: nums = [1,2], operations = [[1,3],[2,1],[3,2]]
Output: [2,1]
Explanation: We perform the following operations to nums:
- Replace the number 1 with 3. nums becomes [3,2].
- Replace the number 2 with 1. nums becomes [3,1].
- Replace the number 3 with 2. nums becomes [2,1].
We return the array [2,1].

Solution:
    - Use a hashmap number:index


Created on July 10, 2022
@author: smaiya
'''
from typing import Dict, Any, List


class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        nums_dict = {}
        nums_dict = {n:i for i, n in enumerate(nums)}
        for op in operations:
            frm, to = op[0], op[1]
            idx = nums_dict[frm]
            nums_dict[to] = idx
            nums[idx] = to
            nums_dict.pop(frm)
        return nums



nums = [1,2,4,6]
operations = [[1,3],[4,7],[6,1]]
ans = Solution().arrayChange(nums, operations)