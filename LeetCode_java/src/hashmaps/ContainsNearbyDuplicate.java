/*
 * Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] 
 * and the absolute difference between i and j is at most k.
 Example:
 Input: nums = [1,2,3,1], k = 3
 Output: true

 Input: nums = [1,0,1,1], k = 1
 Output: true

 Input: nums = [1,2,3,1,2,3], k = 2
 Output: false

Solution: 
	- Hashmap to store the unique numbers as the key and the 'latest' index as the value
 */

package hashmaps;

import java.util.HashMap;
import java.util.Map;

public class ContainsNearbyDuplicate {
	public boolean containsNearbyDuplicate(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<Integer, Integer> ();
        for (int i=0; i<nums.length; i++){
            if (map.containsKey(nums[i]) && (i-map.get(nums[i]))<=k)
                return true;
            else
                map.put(nums[i], i);
        }
        return false;
    }
}
