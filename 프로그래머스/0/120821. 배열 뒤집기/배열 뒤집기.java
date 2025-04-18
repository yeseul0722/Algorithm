class Solution {
    public int[] solution(int[] num_list) {
        int n = num_list.length;
        int m = 0;
        int[] answer = new int[n];
        for (int i = n - 1; i >= 0; i-- ) {
            answer[m] = num_list[i];
            m++;
        }
        return answer;
    }
}