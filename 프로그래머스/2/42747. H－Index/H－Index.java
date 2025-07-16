import java.util.*;

class Solution {
    public int solution(int[] citations) {
      
        int n = citations.length;
        Arrays.sort(citations);
        
        for (int i = 0; i < n; i++) {
            int h = n - i;
            if (h <= citations[i]) {
                return h;
            };
        };
        
        return 0;
    }
}