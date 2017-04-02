import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner in = new Scanner(System.in);

        String binary = "";

        //int input = in.nextInt();
        int input = 439;
        if (input != 0) {
            while(input > 0) {
                binary = binary + Integer.toString(input % 2);
                input = input / 2;
            }
        } else {
            binary = "0";
        }

        int consecutiveOnes = 0;
        int maxValue = 0;
        for (int i=0; i < binary.length(); i++) {
            if (binary.charAt(i) == '1') {
                consecutiveOnes++;
                if (consecutiveOnes > maxValue) {
                    maxValue = consecutiveOnes;
                }
            } else {
                consecutiveOnes = 0;
            }
        }

        System.out.println(binary);
        System.out.println(consecutiveOnes);


    }
}
