def solution(routes):
    answer = 0
    routes.sort(key = lambda x:x[1])
    key = -30001
    
    for route in routes:
        if route[0] > key:
            key = route[1]
            answer += 1
    return answer