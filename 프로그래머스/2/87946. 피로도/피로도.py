from itertools import permutations

def solution(k, dungeons):
    answer = 0
    hp = k
    for permute in permutations(dungeons, len(dungeons)):
        temp_count = 0
        hp = k
        for pm in permute:
            if hp >= pm[0]:
                hp -= pm[1]
                temp_count += 1
        answer = max(answer, temp_count)

    return answer