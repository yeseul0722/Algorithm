def solution(picks, minerals):
    answer = 0
    tools = sum(picks)
    if len(minerals) > tools * 5:
        minerals = minerals[:tools * 5]
    
    new_minerals = [[0, 0, 0] for _ in range(len(minerals) // 5 + 1)]
    for m in range(len(minerals)):
        if minerals[m] == 'diamond':
            new_minerals[m // 5][0] += 1
        elif minerals[m] == 'iron':
            new_minerals[m // 5][1] += 1
        else:
            new_minerals[m // 5][2] += 1
            
    new_minerals.sort(key = lambda x : (-x[0], -x[1], -x[2]))
    
    for dia, iron, stone in new_minerals:
        for i in range(3):
            if picks[i] > 0 and i == 0:
                answer += dia + iron + stone
                picks[i] -= 1
                break
            if picks[i] > 0 and i == 1:
                answer += dia * 5 + iron + stone
                picks[i] -= 1
                break
            if picks[i] > 0 and i == 2:
                answer += dia * 25 + iron * 5 + stone
                picks[i] -= 1
                break
    
    return answer