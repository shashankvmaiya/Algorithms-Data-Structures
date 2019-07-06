package trees;

import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;
import java.util.Queue;

public class IsCousins {
	// Definition for a binary tree node.
	class TreeNode {
		int val;
		TreeNode left;
		TreeNode right;

		TreeNode(int x) {
			val = x;
		}
	}
	
	public boolean isCousins(TreeNode root, int x, int y) {
        Map <Integer, Integer> depth = new HashMap<> ();
        Map <Integer, Integer> parent = new HashMap<> ();
        if (x == root.val || y == root.val)
        		return false;
        
        Queue <TreeNode> q = new LinkedList <> ();
        int d = 0; 
        q.add(root);
        while (!q.isEmpty()) {
        		d++;
        		int count = q.size();
        		for (int i=0; i<count; i++) {
        			TreeNode n = q.poll();
        			
        			if (n.left != null) {
            			q.add(n.left);
            			if (n.left.val == x || n.left.val == y) {
            				depth.put(n.left.val, d+1);
            				parent.put(n.left.val, n.val);
            			}
            		}
        			if (n.right != null) {
            			q.add(n.right);
            			if (n.right.val == x || n.right.val == y) {
            				depth.put(n.right.val, d+1);
            				parent.put(n.right.val, n.val);
            			}
            		}
        		}
        }
        if (!depth.containsKey(x) || !depth.containsKey(y))
        		return false;
        return ((depth.get(x) == depth.get(y)) && (parent.get(x) != parent.get(y))); 
    }

}
