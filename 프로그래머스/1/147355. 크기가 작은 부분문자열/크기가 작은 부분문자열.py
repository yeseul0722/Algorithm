def solution(t, p):
    answer = 0
    n = len(p)
    start, end = 0, n
    
    while end <= len(t):
        if int(t[start : end]) <= int(p):
            answer += 1
        start += 1
        end += 1
    return answer