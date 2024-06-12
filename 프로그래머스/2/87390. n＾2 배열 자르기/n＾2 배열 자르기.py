def solution(n, left, right):
    answer = []
    
    for i in range(left, right + 1):
        num = max((i // n), (i % n)) + 1
        answer.append(num)
    return answer