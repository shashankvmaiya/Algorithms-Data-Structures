/*
 * Given two arrays, write a function to compute their intersection.
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]

Solution: 
	- Use 2 Hashsets
		- First one stores the unique element of the first array
 */

package hashmaps;

import java.util.HashSet;
import java.util.Set;

public class SetIntersection {
	public int[] intersection(int[] nums1, int[] nums2) {
        Set<Integer> set = new HashSet<Integer> ();
        Set<Integer> intersection_set = new HashSet<Integer> ();
        
        for (int num: nums1) {
        		set.add(num);
        }
        for (int num: nums2) {
        		if (set.contains(num))
        			intersection_set.add(num);
        }
        // Integer[] result = intersection_set.toArray(new Integer[intersection_set.size()]);
        // Converting Hashset to int[]
        int[] result = intersection_set.stream().mapToInt(Integer::intValue).toArray();
        return result;
    }
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
