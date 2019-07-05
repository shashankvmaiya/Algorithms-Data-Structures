/*
 * Given two strings s and t , write a function to determine if t is an anagram of s.
Input: s = "anagram", t = "nagaram"
Output: true

Input: s = "rat", t = "car"
Output: false

Solution: 
	- Use Hashmap: Key = letters, Value = Letter count
 */

package hashmaps;

import java.util.HashMap;
import java.util.Map;

public class IsAnagram {
	public boolean isAnagram(String s, String t) {
        if (s.length() != t.length())
            return false;
        Map<Character, Integer> map = new HashMap<Character, Integer>();
        for (char c: s.toCharArray()){
            map.put(c, map.getOrDefault(c, 0)+1);
        }
        for (char c:t.toCharArray()){
            if (map.containsKey(c) && map.get(c)>0){
                map.put(c, map.get(c)-1);
            }
            else{
                return false;
            }
        }
        return true;
    }
}
