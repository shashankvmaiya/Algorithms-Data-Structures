/*
 * Given a n-ary tree, find its maximum depth.
 * The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
 * 
Solution: 
	- Do a DFS: Maintain the depth of the current level and update the depth when visiting each node
	- BFS would work too
 */

package trees;

import java.util.List;

public class NaryMaxDepth {
	//Definition for a Node.
	class Node {
	 public int val;
	 public List<Node> children;

	 public Node() {}

	 public Node(int _val,List<Node> _children) {
	     val = _val;
	     children = _children;
	 }
	};
	
	int max_depth;
    public int maxDepth(Node root) {
    		if (root == null)
    			return 0;
        max_depth = 1;
        dfs(root, 1);
        return max_depth;
    }
    
    public void dfs(Node node, int depth) {
    		if (node == null)
    			return;
    		max_depth = depth>max_depth? depth:max_depth;
    		if (node.children != null) {
    			for (Node child:node.children)
        			dfs(child, depth+1);	
    		}
    }
}
