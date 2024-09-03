from itertools import permutations
def solution(k, dungeons):
    answer = 0
    
    for permute in permutations(dungeons, len(dungeons)):
        cnt = 0
        hp = k
        for p in permute:
            if hp >= p[0]:
                hp -= p[1]
                cnt += 1
        answer = max(answer, cnt)
        
    return answer