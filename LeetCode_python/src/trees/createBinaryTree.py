
'''
You are given a 2D integer array descriptions where descriptions[i] = [parenti, childi, isLefti] 
indicates that parenti is the parent of childi in a binary tree of unique values. Furthermore,

If isLefti == 1, then childi is the left child of parenti.
If isLefti == 0, then childi is the right child of parenti.
Construct the binary tree described by descriptions and return its root.

Solution:
    - Create a graph: key = parent node and values = left and right child nodes
    - Obtain the root node by checking which among the keys in the graph has no parent
    - Use BFS to construct the graph

Created on June 11, 2022
@author: smaiya
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def createBinaryTree(self, descriptions):
        graph = {}
        not_root = set()
        for d in descriptions:
            not_root.add(d[1])
            if d[0] in graph:
                graph[d[0]].append((d[1], d[2]))
            else:
                graph[d[0]] = [(d[1], d[2])]
                
        root = None
        for n in graph:
            if n not in not_root:
                root = TreeNode(n)
                break
        queue = [root]
        while queue:
            node = queue.pop(0)
            children = graph[node.val] if node.val in graph else []
            left_child, right_child = None, None
            for val, is_left in children:
                if is_left:
                    left_child = TreeNode(val)
                else:
                    right_child = TreeNode(val)
            if left_child:
                node.left = left_child
                queue.append(left_child)
            if right_child:
                node.right = right_child
                queue.append(right_child)
        
        return root

descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
root = Solution().createBinaryTree(descriptions)
