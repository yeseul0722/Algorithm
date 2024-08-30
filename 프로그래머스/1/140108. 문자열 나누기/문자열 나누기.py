def solution(s):
    answer = 0
    x = ''
    cnt1, cnt2 = 0, 0
    for i in s:
        if cnt1 == cnt2:
            answer += 1
            x = i
            cnt1, cnt2 = 0, 0
        if i == x:
            cnt1 += 1
        else:
            cnt2 += 1
        
    return answer