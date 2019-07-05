package hashmaps;

import java.util.HashMap;
import java.util.Map;

public class WordPattern {
	public boolean wordPattern(String pattern, String str) {
        Map<Character, String> map = new HashMap<Character, String>();
        String[] words = str.split(" ");
        if (pattern.length() != words.length)
        		return false; 
        for (int i=0; i<pattern.length(); i++) {
        		char c = pattern.charAt(i);
        		String word = words[i];
        		if (map.containsKey(c) && !map.get(c).equals(word))
        			return false;
        		else
        			if (!map.containsKey(c) && map.containsValue(word))
        				return false;
        			map.put(c,  word);
        }
        return true;
	}
	public static void main(String[] args) {
		String pattern = "abba";
		String str = "dog cat cat dog";
		WordPattern wp = new WordPattern();
		boolean result = wp.wordPattern(pattern,  str);
		System.out.println("Result: "+result);
	}
}
