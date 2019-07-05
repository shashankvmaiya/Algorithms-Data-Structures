/* Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"

Solution: 
	- Use a hashmap to store the count of each character required to form T
	- Use two pointers - left and right - which would correspond to a window in S that contains all the characters in T
	- First move right pointer till we get a window that contains all character
	- Then move the left pointer till we remove the first element that would result in violation
	- Violation is when count < length(T)
 */


package hashmaps;

import java.util.HashMap;
import java.util.Map;

public class MinimumWindowSubstring {
	public String minWindow(String s, String t) {
		
		// map stores the count of each character remaining to form the pattern t
        Map<Character, Integer> map = new HashMap<Character, Integer>();
        for (char c: t.toCharArray()) {
        		map.put(c, map.getOrDefault(c, 0)+1);
        }
        
        /*
        if (t.length()==1) {
        		if (map.containsKey(t.charAt(0)))
        			return t;
        		else
        			return "";
        }
        */
        
        int count = 0; // count stores the number of character in pattern t, that is contained within the s[left, right] window
        int left = 0;
        String result = "";
        for (int right=0; right<s.length(); right++) {
        		char c = s.charAt(right);
        		
        		// Move the right pointer till count == t.length()
	        	if (map.containsKey(c)) {
	    			map.put(c, map.get(c)-1);
	    			// Count is updated only when that character is still required for the pattern
	    			if (map.get(c)>=0)
	    				count+=1;
	    		}
	        	
	        	// Move the left pointer till we reach the first character for which the pattern cannot be formed in the window
	        	while (count == t.length()) {
	        		// Store the result 
	        		if (result.length()==0 || right-left+1<result.length())
	        			result = s.substring(left,  right+1);
	        		c = s.charAt(left);
	        		if (map.containsKey(c)) {
	        			map.put(c,  map.get(c)+1);
	        			// Only when map[c] > 0, a relevant character in the pattern is removed. Hence we decrement count
	        			if (map.get(c)>0)
	        				count-=1;
	        		}
	        		left+=1;
	        	}
        }
        return result;
    }
}
