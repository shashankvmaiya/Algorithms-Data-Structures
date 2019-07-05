/*
 * Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. 
 * Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.
 * 
Input: [3, 1, 4, 1, 5], k = 2
Output: 2

Input: [1, 3, 1, 5, 4], k = 0
Output: 1

Solution: 
	- Use a HashMap and handle k=0 and k>0 separately
	- For k=0, we have to find the number of repetitions
	- For k>0, we have to only consider the unique instances of the numbers in the set
 */
package hashmaps;

import java.util.HashMap;
import java.util.Map;

public class KDiffPairsInArray {
	public int findPairs(int[] nums, int k) {
		// Absolute difference cannot be < 0
		if (k<0)
			return 0;
        Map <Integer, Integer> map = new HashMap <Integer, Integer>();
        int count = 0;
        for (int num: nums) {
        		map.put(num,  map.getOrDefault(num,  0)+1);
        		// If k=0, increment count if there is a repetition
        		if (k==0 && map.get(num)==2)
        			count++;
        		// If k>0, modify count only for the first occurence of a number
        		if (k!=0 && map.get(num)==1) {
        			if (map.containsKey(num+k))
        				count++;
        			if(map.containsKey(num-k))
        				count++;
        		}
        }
        return count;
    }
}
