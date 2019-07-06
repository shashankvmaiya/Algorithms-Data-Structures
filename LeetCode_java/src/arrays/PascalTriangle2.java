package arrays;

import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

public class PascalTriangle2 {
	public List<Integer> getRow(int rowIndex) {
        if (rowIndex==0)
        		return new ArrayList<> (Arrays.asList(1));
        List<Integer> ping = new ArrayList<> (Arrays.asList(1, 1));
        if (rowIndex==1)
    			return ping;
        List<Integer> pong = new ArrayList<>();
        for (int i=2; i<=rowIndex; i++) {
        		if (i%2==0) {
        			pong.clear();
        			pong.add(1);
            		for (int j=1; j<i; j++) 
            			pong.add(ping.get(j)+ping.get(j-1));
            		pong.add(1);
        		}
        		else {
        			ping.clear();
        			ping.add(1);
            		for (int j=1; j<i; j++) 
            			ping.add(pong.get(j)+pong.get(j-1));
            		ping.add(1);
        		}
        }
        if (rowIndex%2==0)
        		return pong;
        else
        		return ping;
    }
	public static void main(String[] args) {
		PascalTriangle2 pt = new PascalTriangle2();
		System.out.println("Pascal Row 0: "+pt.getRow(0));
		System.out.println("Pascal Row 1: "+pt.getRow(1));
		System.out.println("Pascal Row 3: "+pt.getRow(3));
	}
}
