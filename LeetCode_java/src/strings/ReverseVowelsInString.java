/*
 * Write a function that takes a string as input and reverse only the vowels of a string.
Input: "hello"
Output: "holle"

Solution: 
	- Use StringBuilder and swap the vowels 

 */

package strings;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class ReverseVowelsInString {
	public String reverseVowels(String s) {
        Set<Character> set = new HashSet<Character>(Arrays.asList('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'));
        if (s.length()<=1)
        		return s;
        int left = 0;
        int right = s.length()-1;
        StringBuilder sb = new StringBuilder(s);
        while (left<right) {
        		char cl = s.charAt(left);
        		char cr = s.charAt(right);
        		if (set.contains(cl) && set.contains(cr)) {
        			sb.setCharAt(left, cr);
        			sb.setCharAt(right, cl);
        			left++;
        			right--;
        		}
        		else if (!set.contains(cl)) {
        			left++;
        		}
        		else if (!set.contains(cr)) {
        			right--;
        		}
        		
        }
        return sb.toString();
    }
}
