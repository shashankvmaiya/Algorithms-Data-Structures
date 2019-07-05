/*
 * Given an array of integers, find if the array contains any duplicates.

Input: [1,2,3,1]
Output: true
Input: [1,2,3,4]
Output: false

Solution: 
	- Use a HashSet to store unique numbers
 */

package hashmaps;

import java.util.HashSet;
import java.util.Set;

public class ContainsDuplicate {
	public boolean containsDuplicate(int[] nums) {
        Set <Integer> set = new HashSet<Integer> ();
        for (int num: nums){
            if (set.contains(num))
                return true;
            set.add(num);
        }
        return false;
    }
}
