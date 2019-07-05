/*
 * Given two strings s and t, determine if they are isomorphic.
 * Two strings are isomorphic if the characters in s can be replaced to get t.
 * Examples: 
Input: s = "egg", t = "add"
Output: true

Input: s = "foo", t = "bar"
Output: false

Input: s = "paper", t = "title"
Output: true

Solution: 
	- Use Hashmap to store the encoding of character
	- Use a Hashset to store the character that have already been used from the second string
 */

package hashmaps;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class IsomorphicStrings {
	public boolean isIsomorphic(String s, String t) {
        Map<Character, Character> map = new HashMap<Character, Character> ();
        Set<Character> set = new HashSet<Character> ();
        for (int i=0; i<s.length(); i++){
            Character c1 = s.charAt(i);
            Character c2 = t.charAt(i);
            if (map.containsKey(c1)){
            		/* Check if the character map is the same as it was before */
                if (map.get(c1)!=c2){
                    return false;
                }
            }
            else{
            		/* If it's a new character in map -> check if it was previously used in the string 't' */
                if (set.contains(c2))
                    return false;
                map.put(c1, c2);
                set.add(c2);
            }
        }
        return true;
    }
}
