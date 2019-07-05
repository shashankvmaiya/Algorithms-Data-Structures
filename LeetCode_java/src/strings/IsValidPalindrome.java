/*
 * Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Input: "A man, a plan, a canal: Panama"
Output: true

Input: "race a car"
Output: false

Solution: 
	- Use the inbuilt Character.isLetterOrDigit function to consider only the alphanumeric characters
 */

package strings;

public class IsValidPalindrome {
	public boolean isPalindrome(String s) {
		
		int left = 0;
        int right = s.length()-1;
        s = s.toLowerCase();
        while (left<right) {
        		char cl = s.charAt(left);
        		char cr = s.charAt(right);
        		if (!Character.isLetterOrDigit(cl))
        			left++;
        		if (!Character.isLetterOrDigit(cr))
        			right--;
        		if (Character.isLetterOrDigit(cl) && Character.isLetterOrDigit(cr)) {
        			if (cl==cr) {
        				left++;
        				right--;
        			}
        			else
        				return false;
        		}
        }
        return true;
    }
	public static void main(String[] args) {
		IsValidPalindrome p = new IsValidPalindrome();
		System.out.println("Is Valid: "+ p.isPalindrome("0P"));
	}
}
