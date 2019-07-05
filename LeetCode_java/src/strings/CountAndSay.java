/*
 * The count-and-say sequence is the sequence of integers with the first five terms as following:
1.     1
2.     11
3.     21
4.     1211
5.     111221
Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.
Input: 4
Output: "1211"

Solution: 
	- Kind of Brute Force Solution: Use StringBuilder and generate the CountAndSay string starting from 1 to n 
 */

package strings;

public class CountAndSay {
	public String countAndSay(int n) {
        StringBuilder prev = new StringBuilder("1");
        if (n==1)
        		return prev.toString();
        
        StringBuilder curr = null;
        for (int i=1; i<n; i++) {
        		curr = new StringBuilder();
        		for (int j=0; j<prev.length();) {
        			int count = 0;
        			char c = prev.charAt(j);
        			while (j<prev.length() && prev.charAt(j)==c) {
        				count+=1;
        				j+=1;
        			}
        			curr.append(count).append(c);
        		}
        		prev = curr;
        }
        return curr.toString();
    }
}
