def solution(n):
    answer = []
    
    while n :
        rest = n % 3
        if not rest:
            rest = 4
            n -= 1
        answer.append(str(rest))
        n //= 3
        
    return  ''.join(answer[:: -1])