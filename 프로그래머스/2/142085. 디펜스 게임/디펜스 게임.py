from heapq import heappop, heappush
def solution(n, k, enemy):
    answer, sum_enemy = 0, 0
    heap = []
    
    for e in enemy:
        heappush(heap, -e)
        sum_enemy += e
        if sum_enemy > n:
            if k == 0:
                break
            sum_enemy += heappop(heap)
            k -= 1
        answer += 1
        
    return answer