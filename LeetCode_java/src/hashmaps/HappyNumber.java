/*
 * Write an algorithm to determine if a number is "happy".
 * Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat 
 * the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. 
 * Those numbers for which this process ends in 1 are happy numbers.
Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

Solution: 
	- Use a HashSet to store all the unique numbers formed by sum of the square of digits
	- If repeated, then not a happy number
 */

package hashmaps;

import java.util.HashSet;
import java.util.Set;

public class HappyNumber {

    public boolean isHappy(int n) {
        Set<Integer> set = new HashSet<Integer>();
        while (true){
            n = split_square_sum(n);
            if (n==1)
                return true;
            if (set.contains(n))
                return false;
            set.add(n);
        }
    }
    int split_square_sum(int num){
        int result = 0;
        while(num!=0){
            result+=Math.pow(num%10, 2);
            num/=10;
        }
        return result;
    }
}
