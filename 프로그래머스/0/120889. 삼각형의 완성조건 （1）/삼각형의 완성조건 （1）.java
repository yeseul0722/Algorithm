import java.util.*;

class Solution {
    public int solution(int[] sides) {
        Arrays.sort(sides);
        if (sides[2] < sides[1] + sides[0]) {
            return 1;
        }
        else {
            return 2;
        }
    }
}