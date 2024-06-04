def solution(scores):
    answer = 0
    wan_a, wan_b = scores[0]
    wan_score = wan_a + wan_b
    max_b = 0
    scores.sort(key = lambda x:(-x[0], x[1]))
    
    for a, b in scores:
        if wan_a < a and wan_b < b:
            return -1
        else:
            if b >= max_b:
                max_b = b
                if a + b > wan_score:
                    answer += 1
                
    return answer + 1