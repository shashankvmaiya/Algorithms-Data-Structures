/*
 * Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
 * 
Solution: 
	- Use Breadth First Search using Queue
 */

package trees;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class NaryLevelOrderTraversal {
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
	
	public List<List<Integer>> levelOrder(Node root) {
        List<List<Integer>> result = new ArrayList<>();
        if (root == null)
        		return result;
        Queue<Node> q = new LinkedList<Node> ();
        q.add(root);
        while(!q.isEmpty()) {
        		List<Integer> list = new ArrayList<> ();
        		int length = q.size();
        		for (int i=0; i<length; i++) {
        			Node n = q.poll();
        			list.add(n.val);
        			if (n.children != null) {
        				for (Node nc: n.children)
        					q.add(nc);
        			}
        		}
        		result.add(list);
        }
        return result;
    }
}
