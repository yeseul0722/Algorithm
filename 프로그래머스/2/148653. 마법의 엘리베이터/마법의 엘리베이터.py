def solution(storey):
    answer = 0
    while storey:
        now = storey % 10
        if now > 5:
            answer += 10 - now
            storey += 10
        elif now < 5:
            answer += now
        else:
            if (storey // 10) % 10 >= 5:
                storey += 10
            answer += 5
            
        storey //= 10
        
    return answer