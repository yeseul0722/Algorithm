class Solution {
    public int solution(String str1, String str2) {
        int n = str1.length();
        int m = str2.length();
        
        for (int i = 0; i < n - m + 1; i++) {
            if (str1.substring(i, i + m).equals(str2)) {
                return 1;
            }
        }
        return 2;
        
    }
}