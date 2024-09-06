def solution(skill, skill_trees):
    answer = 0
    lst = []
    for s in skill_trees:
        temp = ''
        for i in s:
            if i in skill:
                temp += i
        lst.append(temp)
        
    for k in lst:
        n = len(k)
        if k == skill[:n]:
            answer += 1
            
    return answer