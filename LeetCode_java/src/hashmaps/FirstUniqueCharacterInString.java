/*
 * Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

Solution: 
	- Use Hashmap and iterate through the string twice
 */

package hashmaps;

import java.util.HashMap;
import java.util.Map;

public class FirstUniqueCharacterInString {
	public int firstUniqChar(String s) {
        Map<Character, Integer> map = new HashMap<Character, Integer>();
        for (char c: s.toCharArray()) {
        		map.put(c, map.getOrDefault(c,  0)+1);
        }
        for (int i=0; i<s.length(); i++) {
        		if (map.get(s.charAt(i))==1) {
        			return i;
        		}
        }
        return -1;
    }
}
