/*
 * Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
 * If the last word does not exist, return 0.
 * 
Input: "Hello World"
Output: 5
 */

package strings;

public class LengthOfLastWord {
	public int lengthOfLastWord(String s) {
		// Remove all beginning/trailing spaces
		s = s.trim();
		if (s==null || s.length()==0)
			return 0;
		String[] words = s.split(" ");
		return words[words.length-1].length();
    }
}
