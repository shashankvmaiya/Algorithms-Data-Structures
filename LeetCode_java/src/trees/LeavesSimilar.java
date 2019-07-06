/*
 * Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.
 * Two binary trees are considered leaf-similar if their leaf value sequence is the same.
 * Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
 * 
 * Solution: 
 	- Use DFS (pre-order traversal) to obtain the leaf sequence for both the trees and check if they are similar
 */

package trees;

import java.util.ArrayList;
import java.util.List;

public class LeavesSimilar {
	// Definition for a binary tree node.
	class TreeNode {
		int val;
		TreeNode left;
		TreeNode right;

		TreeNode(int x) {
			val = x;
		}
	}
	
	public boolean leafSimilar(TreeNode root1, TreeNode root2) {
        List<Integer> leaves1 = new ArrayList<> ();
        List<Integer> leaves2 = new ArrayList<> ();
		dfs(root1, leaves1);
		dfs(root2, leaves2);
		return leaves1.equals(leaves2);
    }
	
	public void dfs(TreeNode n, List<Integer> leaves) {
		if (n == null)
			return;
		if (n.left == null && n.right == null)
			leaves.add(n.val);
		if (n.left != null)
			dfs(n.left, leaves);
		if (n.right != null)
			dfs(n.right, leaves);
	}
}
