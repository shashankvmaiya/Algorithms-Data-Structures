/*
 * Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes 
 * that can be built with those letters. This is case sensitive, for example "Aa" is not considered a palindrome here.
Input:
"abccccdd"
Output:
7

Solution: 
	- Store the count for each character in a HashMap
	- Longest Palindrome formed by taking max even number of different characters 
	and 1 odd character (if there is a character which has an odd count)  
 */

package hashmaps;

import java.util.HashMap;
import java.util.Map;

public class LongestPalindrome {
	public int longestPalindrome(String s) {
        Map<Character, Integer> map = new HashMap<Character, Integer>();
        
        for (char c: s.toCharArray()) {
        		map.put(c,  map.getOrDefault(c,  0)+1);
        }
        int result = 0;
        boolean odd_flag = false;
        for (Character c: map.keySet()) {
        		result += (map.get(c)/2)*2;
        		if (map.get(c)%2==1)
        			odd_flag = true;
        }
        return result+(odd_flag?1:0);
    }
}
