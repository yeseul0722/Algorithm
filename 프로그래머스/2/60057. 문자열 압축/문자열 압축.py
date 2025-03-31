def solution(s):
    # 최댓값 설정
    answer = 1000
    
    # i자씩 끊기
    for i in range(1, len(s) + 1):
        # 압축한 문자열
        z = ''
        # 갯수 체크
        cnt = 1
        # 첫번째 미리 자르기
        tmp = s[:i]
        
        # i 단위로 나누어서 비교
        for j in range(i, len(s) + i, i):
            if tmp == s[j:j+i]:
                cnt += 1

            else:
                if cnt != 1:
                    z += str(cnt) + tmp

                else:
                    z += tmp
                tmp = s[j:j+i]
                cnt = 1

        if len(z) < answer:
            answer = len(z)
            
    return answer