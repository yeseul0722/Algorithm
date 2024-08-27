def solution(food):
    answer = ''
    for i in range(1, len(food)):
        n = food[i] // 2
        answer += str(i) * n
    rev = answer[:: -1]
    answer += '0'
    
    return answer + rev