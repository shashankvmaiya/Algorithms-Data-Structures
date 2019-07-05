/*
 * Given a non-empty array of integers, every element appears twice except for one. Find that single one.
 * Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
 * 
 * Solution: 
 * 		- Bitwise XOR of all the elements
 *		- All the elements that repeats twice XORs to 0
 */

package bit_manipulation;

class NonRepeatingNumber {
    public int singleNumber(int[] nums) {
        int result = 0;
        for (int num: nums){
            result = result ^ num;
        }
        return result;
    }
    
    public static void main( String[] args) {
    	
    }
    
    
}