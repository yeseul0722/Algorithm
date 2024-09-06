def solution(d, budget):
    answer = 0
    n = len(d)
    d.sort()
    for i in range(n):
        budget -= d[i]
        if budget < 0:
            return i
        
    if budget >= 0:
        return n
    else:
        return n - 1
