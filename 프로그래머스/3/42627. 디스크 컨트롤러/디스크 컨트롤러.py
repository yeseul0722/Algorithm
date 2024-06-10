import heapq
def solution(jobs):
    answer, i, now = 0, 0, 0
    start = -1
    n = len(jobs)
    heap = []
    
    while i < n:
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(heap, [j[1], j[0]])
        
        if len(heap) > 0:
            current = heapq.heappop(heap)
            start = now
            now += current[0]
            answer += now - current[1]
            i += 1
        else:
            now += 1
            
    return answer // n