import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
    
        HashMap<String, Integer> counts = new HashMap<String, Integer>();
        
        for (String name : participant) {
            counts.put(name, counts.getOrDefault(name, 0) + 1);
        }
        
        for (String name : completion) {
            counts.put(name, counts.get(name) - 1);
            if (counts.get(name) == 0) counts.remove(name);
        }
        
        return counts.keySet().iterator().next();
    }
}