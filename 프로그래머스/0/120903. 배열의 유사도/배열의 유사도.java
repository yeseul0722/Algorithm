class Solution {
    public int solution(String[] s1, String[] s2) {
        int answer = 0;
        int n = s1.length;
        int m = s2.length;
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (s1[i].equals(s2[j])) {
                    answer++;
                    break;
                }
            }
        }
        return answer;
    }
}