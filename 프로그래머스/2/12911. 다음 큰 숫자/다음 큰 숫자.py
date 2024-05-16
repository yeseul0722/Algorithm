def solution(n):
    answer = n + 1
    num = bin(n).count('1')
    
    while bin(answer).count('1') != num:
        answer += 1
    return answer