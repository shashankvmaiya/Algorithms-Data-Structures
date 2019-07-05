/*
 * You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing 
 * the row number and column number of the wanted reshaped matrix, respectively.
 * The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.
 * If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; 
 * Otherwise, output the original matrix.
Input: 
nums = 
[[1,2],
 [3,4]]
r = 1, c = 4
Output: 
[[1,2,3,4]]

Solution: 
	- Read the element row wise and insert it into the new array in its location
 */

package arrays;

public class ReshapeMatrix {
	public int[][] matrixReshape(int[][] nums, int r, int c) {
        int[][]result = new int[r][c];
        if (nums.length==0 || r*c != nums.length*nums[0].length)
        		return nums;
        int count = 0;
        for (int i=0; i<nums.length; i++) {
        		for (int j=0; j<nums[0].length; j++) {
        			result[count/c][count%c] = nums[i][j];
        			count++;
        		}
        }
        return result;
    }
}
