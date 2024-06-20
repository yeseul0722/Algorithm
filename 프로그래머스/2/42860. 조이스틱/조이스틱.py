def solution(name):
    answer = 0
    n = len(name)
    # 기본 최소 이동거리
    min_move = n - 1
    # 리스트를 전부 돌면서 최소 이동거리 구해주기
    for i, char in enumerate(name):
        # 알파벳 이동만큼 정답에 더해주기
        # Z는 A에서 Z로 이동 한 번 더 해야하니깐 + 1 해주기
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        
        # 연속된 A의 갯수 구하기
        next = i + 1
        while next < n and name[next] == 'A':
            next += 1
        # 최소 이동거리, A기준 왼쪽으로 이동했을때 거리, A기준 오른쪽으로 이동했을때 거리 중 최솟값 구하기
        min_move = min([min_move, i * 2 + n - next, 2 * (n - next) + i])
        
    #정답에 최소 이동거리 더해주기    
    answer += min_move
    return answer