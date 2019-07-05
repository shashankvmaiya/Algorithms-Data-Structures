/*
 * Given an array A of positive lengths, return the largest perimeter of a triangle with non-zero area, formed from 3 of these lengths.
 * If it is impossible to form any triangle of non-zero area, return 0.
 * 
Input: [3,2,3,4]
Output: 10

Input: [1,2,1]
Output: 0

Solution: 
	- Sort the array and check for Triangle condition starting from the top 3 sides
 */
package maths;

import java.util.Arrays;

public class LargestPerimeter {
	public int largestPerimeter(int[] A) {
        Arrays.sort(A);
        for (int i=A.length-3; i>=0; i--) {
        		if (A[i]+A[i+1]>A[i+2])
        			return (A[i]+A[i+1]+A[i+2]);
        }
        return 0;
    }
}
