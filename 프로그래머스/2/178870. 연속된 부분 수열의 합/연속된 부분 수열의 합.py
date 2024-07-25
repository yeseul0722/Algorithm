def solution(sequence, k):
    n = len(sequence)
    answer = [0, n - 1]
    
    start, end = 0, 0
    now = 0
    
    while end < n:
        now += sequence[end]
        
        while now > k and start <= end:
            now -= sequence[start]
            start += 1
            
        if now == k:
            if answer[1] - answer[0] > end - start:
                answer = [start, end]
                
        end += 1
        
    return answer