'''
2003. Smallest Missing Genetic Value in Each Subtree

There is a family tree rooted at 0 consisting of n nodes numbered 0 to n - 1. You are 
given a 0-indexed integer array parents, where parents[i] is the parent for node i. 
Since node 0 is the root, parents[0] == -1.

There are 105 genetic values, each represented by an integer in the inclusive range [1, 10^5]. 
You are given a 0-indexed integer array nums, where nums[i] is a distinct genetic value for node i.

Return an array ans of length n where ans[i] is the smallest genetic value that is missing 
from the subtree rooted at node i.

The subtree rooted at a node x contains node x and all of its descendant nodes.

Input: parents = [-1,0,1,0,3,3], nums = [5,4,6,2,1,3]
     0[5]
    / \
  1[4] 3[2]
  /    /  \ 
 2[6] 4[1] 5[3]

Output: [7,1,1,4,2,1]
Explanation: The answer for each subtree is calculated as follows:
- 0: The subtree contains nodes [0,1,2,3,4,5] with values [5,4,6,2,1,3]. 7 is the smallest missing value.
- 1: The subtree contains nodes [1,2] with values [4,6]. 1 is the smallest missing value.
- 2: The subtree contains only node 2 with value 6. 1 is the smallest missing value.
- 3: The subtree contains nodes [3,4,5] with values [2,1,3]. 4 is the smallest missing value.
- 4: The subtree contains only node 4 with value 1. 2 is the smallest missing value.
- 5: The subtree contains only node 5 with value 3. 1 is the smallest missing value.

Solution:
    - Only the ancestors of 1 including itself would have missing value = result > 1
    - Initialize result to all 1s
    - Do a traversal for node that contains 1 and its ancestors (until the root node)
    - Mark all the seen nodes in their subtree to 1
    - The missing value = smallest unseen node


Created on June 12, 2022
@author: smaiya
'''

class Solution:
    def smallestMissingValueSubtree(self, parents, nums):
        self.n = len(nums)
        self.result = [1]*self.n
        self.nums = nums
        if 1 not in nums:
            return self.result
        
        self.children = {}
        for i, p in enumerate(parents):
            if i>=0:
                if p in self.children:
                    self.children[p].append(i)
                else:
                    self.children[p] = [i]

        self.seen = [0]*100010
        node = nums.index(1)
        missing = 1
        # Loop from node=1 to the root node to find all the nodes in the subtree
        while node>=0:
            self.dfs(node)
            # missing value only increases as you go higher up in the tree
            # so, sufficient to start from the previous missing value
            while self.seen[missing]:
                missing+=1
            self.result[node] = missing
            node = parents[node]

        return self.result

    def dfs(self, node):
        # Iterate over only the unseen nodes. Since the seen nodes have already been 
        # traversed and all its subtree nodes have been labeled as seen
        if self.seen[self.nums[node]]==0:
            children = self.children[node] if node in self.children else []
            for c in children:
                self.dfs(c)
            self.seen[self.nums[node]] = 1

parents = [-1,0,1,0,3,3]
nums = [5,4,6,2,1,3]
ans = Solution().smallestMissingValueSubtree(parents, nums)
print('Smallest Missing Value Subtree = ', ans)