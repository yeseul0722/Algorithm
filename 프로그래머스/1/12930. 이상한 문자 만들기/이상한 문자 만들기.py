def solution(s):
    answer = ''
    idx = 0
    
    for i in range(len(s)):
        if s[i] == ' ':
            idx = 0
            answer += ' '
        else:
            if idx % 2 == 1:
                answer += s[i].lower()
            else:
                answer += s[i].upper()
            idx += 1
    return answer