
/*
 * Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  
 * Return a list of all possible strings we could create.
 * Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]

Solution: 
	- Use DFS
	- For each character, toggle lowercase and uppercase 
 */


package backtracking;

import java.util.ArrayList;
import java.util.List;

public class LetterCasePermutation {
	public List<String> letterCasePermutation(String S) {
        List<String> result = new ArrayList<> ();
        char[] str = S.toCharArray();
        dfs(str, 0, result);
        return result;
    }
	public void dfs(char[] str, int index, List<String> result) {
		if (index == str.length) {
			result.add(new String(str));
			return;
		}
		if (Character.isAlphabetic(str[index])) {
			str[index] = Character.toLowerCase(str[index]);
			dfs(str, index+1, result);
			str[index] = Character.toUpperCase(str[index]);
			dfs(str, index+1, result);
		}
		else
			dfs(str, index+1, result);
	}
	
	public static void main (String[] args) {
		LetterCasePermutation x = new LetterCasePermutation();
		System.out.println("Permutations: "+x.letterCasePermutation("a1b2"));
	}
}
