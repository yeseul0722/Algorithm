def solution(routes):
    answer = 0
    end = -30001
    routes.sort(key = lambda x:x[1])
    for route in routes:
        if route[0] > end:
            end = route[1]
            answer += 1
    return answer