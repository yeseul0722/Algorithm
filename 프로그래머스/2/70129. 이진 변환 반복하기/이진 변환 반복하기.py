def solution(s):
    cnt = 0
    zero_cnt = 0
    
    # s가 1이 되면 반복문 종료
    while s != '1':

        #1의 갯수 세어주기
        length = s.count('1')
        # 전체 길이 - 1의 갯수 = 0의 갯수
        zero_cnt += len(s) - length
        # s의 길이를 2진수로 변환
        s = str(format(length, 'b'))
        # 변환 횟수 + 1
        cnt += 1

    return [cnt, zero_cnt]