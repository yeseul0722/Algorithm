from itertools import permutations
def solution(k, dungeons):
    answer = 0
    n = len(dungeons)
    for dungeon in permutations(dungeons, n):
        hp = k
        cnt = 0
        for i in dungeon:
            if hp >= i[0]:
                hp -= i[1]
                cnt += 1
            else:
                break
        if cnt > answer:
            answer = cnt
                
    return answer